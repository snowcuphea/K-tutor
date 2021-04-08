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
            return Response("This email is already registered.", status=status.HTTP_406_NOT_ACCEPTABLE)
        if User.objects.filter(nickname=request.data['nickname']).exists():
            return Response("This nickname is already registered.", status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.username = request.data['username']
        user.save()

        achievement_list = Achievement.objects.all()
        for al in achievement_list:
            AchieveManage.objects.create(user=user, achievement=al, done=0)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  View):
    serializer_class = UserSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # 정보 수정
    @swagger_auto_schema(responses={200: "username"}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def put(self, request):
        """
        Modify User Info

        ___
        """
        # 회원 수정한 정보를 request.data에 담았다고 가정
        user = request.user
        if user.nickname != request.data['nickname'] and \
                User.objects.filter(nickname=request.data['nickname']).exists():
            return Response("This nickname is already registered.", status=status.HTTP_302_FOUND)
        user.set_password(request.data['password'])
        user.nickname = request.data['nickname']
        user.save()
        return Response(user.serializable_value(field_name="nickname"), status=status.HTTP_200_OK)

    # 회원 탈퇴
    @swagger_auto_schema(responses={200: "deleted"}, manual_parameters=[
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
        if Lc.objects.filter(learned_user=user).exists():
            recent_cs = Cs.objects.get(pk=data['recent_learned_lc'][0]['cs_id']).__dict__
            if recent_cs['type'] == 'kpop':
                recent_cs['name_kor'] = recent_cs['name_kor'].split(' - ')[0]
                recent_cs['name_eng'] = recent_cs['name_eng'].split(' - ')[0]
        else:
            recent_cs = Cs.objects.get(pk=1).__dict__
        del (recent_cs['_state'])
        data['recent_cs'] = recent_cs
        # recent_lc_progress = serializers.DictField()
        recent_lc_progress = dict()
        for lc in list(user.learned_lc.all()):
            if lc.cs.type == 'kpop':
                singer = lc.cs.name_kor.split(" - ")[0]
                if singer not in recent_lc_progress:
                    recent_lc_progress[singer] = [
                        Lc.objects.filter(cs__name_kor__contains=singer).filter(learned_user=user).count(),
                        Lc.objects.filter(cs__name_kor__contains=singer).count()
                    ]
            else:
                if lc.cs.name_kor not in recent_lc_progress:
                    recent_lc_progress[lc.cs.name_kor] = [
                        Lc.objects.filter(cs__name_kor=lc.cs.name_kor).filter(learned_user=user).count(),
                        Lc.objects.filter(cs__name_kor=lc.cs.name_kor).count()
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
        # serializer = UserSerializer(user)
        return Response('Exp Gained', status=status.HTTP_200_OK)


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

        for acv in achievement_list:
            if not Achievement.objects.filter(Q(achieved_user=user) & Q(id=acv.id)).exists():
                user.achieved.add(acv)
        al = user.achieved.all()
        for acv in al:
            acvm = AchieveManage.objects.get(user=user, achievement=acv)
            if acvm.done >= acv.total:
                user_achievement.append({
                    "achievement_id": acv.id,
                    "title": acv.title,
                    "content": acv.content,
                    "imgurl": acv.imgurl,
                    "done": acvm.done,
                    "total": acv.total,
                    "great_kor": acv.great_kor,
                    "great_eng": acv.great_eng,
                    "great_dsc": acv.great_dsc,
                    "status": 1
                })
            else:
                user_achievement.append({
                    "achievement_id": acv.id,
                    "title": acv.title,
                    "content": acv.content,
                    "imgurl": acv.imgurl,
                    "done": acvm.done,
                    "total": acv.total,
                    "great_kor": acv.great_kor,
                    "great_eng": acv.great_eng,
                    "great_dsc": acv.great_dsc,
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
        achievement = Achievement.objects.get(id=request.data['AcId'])
        ac_manage = AchieveManage.objects.filter(Q(user=user) & Q(achievement=achievement))
        if not ac_manage.exists():
            user.achieved.add(achievement)
            ac_manage = AchieveManage.objects.get(user=user, achievement=achievement)
        else:
            ac_manage = ac_manage[0]

        if ac_manage.done >= achievement.total:
            return Response("Already Achieved", status=status.HTTP_208_ALREADY_REPORTED)
        else:
            ac_manage.done += 1
            ac_manage.save()
            if ac_manage.done >= achievement.total:
                return Response("Achieved", status=status.HTTP_200_OK)
            return Response("Updated", status=status.HTTP_200_OK)


class InquiryViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     View):
    serializer_class = UserSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: "sent"}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def post(self, request):
        """
        Send inquiry email from user to us.

        ___
        """
        user = request.user
        email = EmailMessage(
            request.data['title'],
            body=str(user.username) + "\n " + request.data['content'],
            to=["malmoongchi@gmail.com"]
        )
        email.send()
        return Response("ok", status=status.HTTP_200_OK)
