import random

from django.views import View
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *
from .serializers import *
from klass.models import *


class ExamViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  View):
    serializer_class = ExamSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def get(self, request):
        """
        Take Exam: get 10 problem list

        ___
        """
        user = request.user
        if user.learned_lc.all().count() < 10:
            return Response("Not ready to take exam. Study more card.", status=status.HTTP_406_NOT_ACCEPTABLE)

        pro_list = []

        learned_lc = user.learned_lc.all()
        for lc in random.sample(learned_lc, 4):
            pro_list.append({
                "problem": {
                    "before": lc.before_kor,
                    "main": lc.cpct_kor,
                    "after": lc.after_kor
                },
                "cs": lc.cs.name
            })

        learned_kw = user.learned_kw.all()
        for kw in random.sample(learned_kw, 3):
            lc = random.choice(Lc.objects.filter(main_kw=kw))
            pro_list.append({
                "problem": {
                    "before": lc.before_kor,
                    "main": lc.cpct_kor,
                    "after": lc.after_kor
                },
                "cs": lc.cs.name
            })

        for kw in random.sample(learned_kw, 3):
            cpcq = random.choice(Cpcq.objects.filter(kcq=kw))
            pro_list.append({
                "problem": {
                    "main": cpcq.kor
                },
                "cs": "구어체 말뭉치"
            })

        serializer = ExamSerializer(data=pro_list, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: "ok"}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def post(self, request):
        """
        Send exam result to DB.
        ___
        """
        ExamResult.objects.create(
            user=request.user,
            score=request.data['score']
        )
        while ExamResult.objects.filter(user=request.user).count() > 10:
            ExamResult.objects.filter(user=request.user)[0].delete()
        return Response("ok", status=status.HTTP_200_OK)


class ExamReportViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        View):
    serializer_class = ExamResultSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def get(self, request):
        """
        Get Exam Report
        
        ___
        """
        serializer = ExamResultSerializer(
            data=ExamResult.objects.filter(user=request.user).values(),
            many=True
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
