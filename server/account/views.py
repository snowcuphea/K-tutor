from django.views import View
from rest_framework import status, viewsets, mixins
from django.db.models import Max, Count

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import TestResult, AccessDate
from .serializers import UserSerializer, User, TestResultSerializer, ReportSearializer
from klass.models import *

from django.shortcuts import get_object_or_404

from datetime import date, timedelta


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
    user = get_object_or_404(User, username=request.data['username'])
    if request.method == 'PUT':
        user.set_password(request.data['password'])
        user.save()
    elif request.method == 'DELETE':
        user.delete()
    return Response(user, status=status.HTTP_200_OK)


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


# 접속 날짜 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def access_list(request, user_pk):
    pass


# 총 접속 날짜 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def access_total(request, user_pk):
    pass


# 연속으로 접속 날짜 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def access_consecutive_max(request, user_pk):
    pass


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def login(self, request):
    data = {}
    # consecutive_access_date = serializers.IntegerField()
    user = get_object_or_404(User, username=request.user.username)
    if not AccessDate.objects.filter(user=user).filter(access_at=date.today()).exists():
        AccessDate.objects.create(user=user)
    if AccessDate.objects.filter(user=user).filter(access_at=date.today() - timedelta(days=1)):
        user.consecutive_acess += 1
        user.save()
    data['consecutive_access_date'] = user.consecutive_acess
    # learned_lc_cnt = serializers.IntegerField()
    data['learned_lc_cnt'] = user.learned_lc.all().count()
    # recent_learned_lc = serializers.ListField()
    data['recent_learned_lc'] = list(user.learned_lc.all())
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
            lcs.filter(learned_user=user),
            lcs.count()
        ]
    data['progress'] = progress
    serializer = ReportSearializer(data=data)
    return Response(serializer.data, status=status.HTTP_200_OK)
