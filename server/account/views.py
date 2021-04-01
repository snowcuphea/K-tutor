from django.core.mail import EmailMessage
from django.views import View
from django.db.models import Max, Count, Q
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

from .models import *
from .serializers import *
from klass.models import *

required_exp = [10, 20, 30, 50, 70,
                100, 150, 200, 250, 300,
                400, 500, 600, 750, 1000]


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
        user.set_password(request.data['password'])
        user.nickname = request.data['nickname']
        user.save()
        return Response(user.serializable_value(field_name="username"), status=status.HTTP_200_OK)

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
        return Response("deleted", status=status.HTTP_200_OK)


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
        RecentLearnedLc.objects.filter(Q(user=user) & Q(learned_at__lt=date.today() - timedelta(days=7))).delete()

        # consecutive_access_date = serializers.IntegerField()
        if not AccessDate.objects.filter(Q(user=user) & Q(access_at=date.today())).exists():
            AccessDate.objects.create(user=user)
            if AccessDate.objects.filter(Q(user=user) & Q(access_at=date.today() - timedelta(days=1))):
                user.consecutive_access += 1
                user.save()
        data['user'] = {
            'nickname': user.nickname,
            'level': user.level,
            'exp': user.exp,
            'consecutive_access': user.consecutive_access
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


class GetexpViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    View):
    serializer_class = UserSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: ""}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def post(self, request):
        """
        Gain Exp

        ___
        """
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


class AchievementViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         View):
    serializer_class = AchievedManageSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def get(self, request):
        """
        Get User's Achievement List

        ___
        """
        user = request.user
        achievement_list = Achievement.objects.all()
        user_achievement = []

        for al in achievement_list:
            if al in user.achieved.all():
                user_achievement.append({
                    "achievement_id": al.id,
                    "title": al.title,
                    "content": al.content,
                    "imgurl": al.imgurl,
                    "status": 1
                })
            else:
                user_achievement.append({
                    "achievement_id": al.id,
                    "title": al.title,
                    "content": al.content,
                    "imgurl": al.imgurl,
                    "status": 0
                })

        serializer = AchievedManageSerializer(data=user_achievement, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: "updated"}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def post(self, request):
        """
        Update user's achievement status

        ___
        """
        user = request.user
        user.achieved.add(request.data['AcId'])
        return Response("updated", status=status.HTTP_200_OK)


class InquiryViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         View):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Send inquiry email from user to us.

        ___
        """
        user = request.user
        email = EmailMessage(
            request['title'],
            request['content'],
            from_email=user.email,
            to="malmoongchi@gmail.com"
        )
        email.send()
        return Response("ok", status=status.HTTP_200_OK)
