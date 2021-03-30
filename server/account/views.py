from django.views import View
from django.db.models import Max, Count
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status, viewsets, mixins

from datetime import date, timedelta

from .serializers import *
from klass.models import *
from .models import *

required_exp = [10, 20, 30, 50, 70,
                100, 150, 200, 250, 300,
                400, 500, 600, 750, 1000]


# 로그아웃
def logout(request):
    pass


class SignupViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    View):
    serializer_class = UserSerializer

    # 회원 가입
    def post(self, request):
        """
        Signup

        ___
        """
        if User.objects.filter(username=request.data['username']).exists():
            return Response("이미 가입된 이메일 입니다.", status=status.HTTP_406_NOT_ACCEPTABLE_)
        if User.objects.filter(nickname=request.data['nickname']).exists():
            return Response("이미 가입된 닉네임 입니다.", status=status.HTTP_406_NOT_ACCEPTABLE_)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.username = request.data['username']
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  View):
    serializer_class = UserSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # 정보 수정
    @swagger_auto_schema(responses={200: ""}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def put(self, request):
        """
        Modify User Info

        ___
        """
        # 회원 수정한 정보를 request.data에 담았다고 가정
        user = request.user
        if User.objects.filter(username=request.data['username']).exists():
            return Response("이미 가입된 이메일 입니다.", status=status.HTTP_302_FOUND)
        if User.objects.filter(nickname=request.data['nickname']).exists():
            return Response("이미 가입된 닉네임 입니다.", status=status.HTTP_302_FOUND)
        user.set_password(request.data.password)
        user.nickname = request.data.nickname
        user.save()
        return Response(user, status=status.HTTP_200_OK)

    # 회원 탈퇴
    @swagger_auto_schema(responses={200: ""}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def delete(self, request):
        """
        Delete User

        ___
        """
        user = request.user
        user.delete()
        return Response(user, status=status.HTTP_200_OK)


class LoginViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   View):
    serializer_class = ReportSearializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: ""}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def get(self, request):
        """
        Get User Report

        ___
        """
        data = {}
        user = get_object_or_404(User, username=request.user.username)
        # 최근 학습 데이터 갱신
        RecentLearnedLc.objects.filter(user=user).filter(learned_at__lt=date.today() - timedelta(days=7)).delete()

        # consecutive_access_date = serializers.IntegerField()
        if not AccessDate.objects.filter(user=user).filter(access_at=date.today()).exists():
            AccessDate.objects.create(user=user)
        if AccessDate.objects.filter(user=user).filter(access_at=date.today() - timedelta(days=1)):
            user.consecutive_acess += 1
            user.save()
        data['user'] = {
            'nickname': user.nickname,
            'level': user.level,
            'exp': user.exp
        }
        # learned_lc_cnt = serializers.IntegerField()
        data['learned_lc_cnt'] = user.learned_lc.all().count()
        # recent_learned_lc = serializers.ListField()
        data['recent_learned_lc'] = list(user.learned_lc.all().order_by('-pk').values())
        # recent_lc_progress = serializers.DictField()
        recent_lc_progress = dict()
        for lc in list(user.learned_lc.all()):
            if lc.cs.name not in recent_lc_progress:
                recent_lc_progress[lc.cs.name] = [
                    Lc.objects.filter(cs__name=lc.cs.name).filter(learned_user=user).count(),
                    Lc.objects.filter(cs__name=lc.cs.name).count()
                ]
        data['recent_lc_progress'] = recent_lc_progress
        # progress = serializers.DictField()
        progress = dict()
        for type in ['drama', 'movie', 'kpop']:
            css = Cs.objects.filter(type=type)
            lcs = Lc.objects.filter(cs__in=css)
            progress[type] = [
                lcs.filter(learned_user=user).count(),
                lcs.count()
            ]
        data['progress'] = progress
        serializer = ReportSearializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# (유저의) 전체 시험 성적 조회, 등록
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def result_list_create(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.method == 'POST':
        TestResult.objects.create(
            user=user,
            score=request.data['score'],
        )
        data = {
            'score': request.data['score']
        }
        serializer = TestResultSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        results = TestResult.objects.filter(user=user)
        serializer = TestResultSerializer(results, many=True)
        return Response(serializer.data)


# 최고 시험 성적 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def result_max(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'GET':
        result = TestResult.objects.aggregate(max_score=Max('score'))
        serializer = TestResultSerializer(result)
        return Response(serializer.data)


# 최근 시험 성적 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def result_latest(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'GET':
        result = TestResult.objects.last()
        serializer = TestResultSerializer(result)
        return Response(serializer.data)


# 레벨업 관련
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def level_up(request):
    pass


# 업적 정보 가져오기, 업적 달성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def acheivement_list_info(request):
    pass
