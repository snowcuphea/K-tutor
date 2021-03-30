from django.views import View
from django.db.models import Max, Count
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status, viewsets, mixins

from datetime import date, timedelta

from .models import *
from .serializers import *
from klass.models import *


required_exp = [10, 20, 30, 50, 70,
                100, 150, 200, 250, 300,
                400, 500, 600, 750, 1000]


# 로그아웃
@api_view(['POST'])
def logout(request):
    pass


# 회원 가입
@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# 정보 수정, 회원 탈퇴
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def account_modify_delete(request):
    # 회원 수정한 정보를 request.data에 담았다고 가정
    user = get_object_or_404(User, email=request.data['email'])
    if request.method == 'PUT':
        user.set_password(request.data['password'])
        user.save()
    elif request.method == 'DELETE':
        user.delete()
    return Response(user, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def login(request):
    data = {}
    user = get_object_or_404(User, username=request.user.username)
    # 최근 학습 데이터 갱신
    Recent_learned_lc.objects.filter(user=user).filter(learned_at__lt=date.today() - timedelta(days=7)).delete()

    # consecutive_access_date = serializers.IntegerField()
    if not AccessDate.objects.filter(user=user).filter(access_at=date.today()).exists():
        AccessDate.objects.create(user=user)
    if AccessDate.objects.filter(user=user).filter(access_at=date.today() - timedelta(days=1)):
        user.consecutive_access += 1
        user.save()
    data['consecutive_access_date'] = user.consecutive_access
    # learned_lc_cnt = serializers.IntegerField()
    data['learned_lc_cnt'] = user.learned_lc.all().count()
    # recent_learned_lc = serializers.ListField()
    data['recent_learned_lc'] = list(user.learned_lc.all().order_by('-pk'))
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
    if serializer.is_valid():
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


# 경험치 획득, 레벨업
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_exp(request):
    user = request.user
    if user.level == 15:
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    user.exp += request.data['exp']
    if required_exp[user.level - 1] <= user.exp:
        user.exp -= required_exp[user.level - 1]
        user.level += 1
        if user.level == 15:
            user.exp = 0
    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 업적 정보 가져오기, 업적 달성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def achievement_list_unlock(request):
    user = request.user
    if request.method == 'GET':
        users_achievements = UserUnlockedAchievement.objects.filter(user=user)
        serializer = UserAchievementSerializer(users_achievements, many=True)
        return Response(serializer.data)