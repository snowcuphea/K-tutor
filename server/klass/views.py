import operator
from functools import reduce

from django.http import Http404
from django.views import View
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .data_update import *
from .serializers import *
from exam.serializers import *

from account.models import RecentLearnedLc
from django.db.models import Q


@api_view(['GET'])
def updateDB(request):
    # update()
    # create_lc()
    # add_meaning_to_lc()
    updateLc()
    return Response("OK", status=status.HTTP_200_OK)


class CsViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                View):
    serializer_class = CsSerializer

    def get_queryset(self):
        conditions = {
            'id': self.kwargs.get("id", None),
            'name__contains': self.request.GET.get('name', None),
            'type__contains': self.request.GET.get('type', None),
        }
        conditions = {key: val for key, val in conditions.items() if val is not None}
        cs = Cs.objects.filter(**conditions)
        if not cs.exists():
            raise Http404()
        return cs

    def get(self, request):
        """
        Cs(Cultural Source) List

        ___
        """
        song_list = Cs.objects.filter(type="kpop")
        cs_list_temp = list(set({x.name.split(" - ")[0] for x in song_list}))
        cs_list = []
        for cs in cs_list_temp:
            cs_list.append({
                "name": cs,
                "type": "kpop",
                "level": song_list.filter(name__contains=cs)[0].level
            })
        cs_list.extend(Cs.objects.filter(type__in=['drama', 'movie']).values())
        serializer = CsSerializer(data=cs_list, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LcListViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    View):
    serializer_class = LcSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        conditions = {
            'id': self.kwargs.get("music_num", None),
        }
        conditions = {key: val for key, val in conditions.items() if val is not None}

        lc = Lc.objects.filter(**conditions)
        if not lc.exists():
            raise Http404()
        return lc

    @swagger_auto_schema(responses={200: "OK"}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def get(self, request, type, title):
        """
        Lc(Learning Card) List

        ___
            - <str:type>: drama, kpop, movie
            - <str:title>: 사이코지만괜찮아, 갓세븐...
        """
        if type != 'kpop':
            cs = get_object_or_404(Cs, name=title)
            lcs = list(Lc.objects.filter(cs=cs).values())
        else:
            css = Cs.objects.filter(name__contains=title)
            lcs = list(Lc.objects.filter(cs__in=css).values())
        user = request.user
        for lc in lcs:
            lc['already_learned'] = True if Lc.objects.filter(Q(learned_user=user) & Q(id=lc['id'])).exists() else False

        serializer = LcSerializer(data=lcs, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LcViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                View):
    serializer_class = LcSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        conditions = {
            'id': self.kwargs.get("music_num", None),
        }
        conditions = {key: val for key, val in conditions.items() if val is not None}

        lc = Lc.objects.filter(**conditions)
        if not lc.exists():
            raise Http404()

        return lc

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def get(self, request, LcId):
        """
        Get Lc

        ___
            - <int:LcId>
        """
        lc = get_object_or_404(Lc, id=LcId).__dict__
        lc['already_learned'] = True if Lc.objects.filter(
            Q(learned_user=request.user) & Q(id=lc['id'])).exists() else False
        serializer = LcSerializer(lc)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: "OK"}, manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def done(self, request, LcId):
        """
        User Learned Lc, Kw

        ___
            - <int:LcId>
        """
        user = request.user
        lc = get_object_or_404(Lc, id=LcId)
        user.learned_lc.add(lc)
        user.learned_kw.add(lc.main_kw)
        if not RecentLearnedLc.objects.filter(Q(user=user) & Q(lc=lc)).exists():
            RecentLearnedLc.objects.create(user=user, lc=lc)
        return Response("ok", status=status.HTTP_200_OK)


class QuizViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  View):
    serializer_class = ExamSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('header_token', openapi.IN_HEADER, description="token must contain jwt token",
                          type=openapi.TYPE_STRING)])
    def get(self, request, type, title):
        """
        Take Quiz: get 5 problem

        ___
        """
        user = request.user
        if type != 'kpop':
            cs = get_object_or_404(Cs, name=title)
            lcs = Lc.objects.filter(cs=cs)
        else:
            css = Cs.objects.filter(name__contains=title)
            lcs = Lc.objects.filter(cs__in=css)

        if lcs.filter(learned_user=user).count() < 5:
            return Response("Not ready to take quiz. Study more card.", status=status.HTTP_406_NOT_ACCEPTABLE)

        pro_list = []

        learned_lc = list(lcs.filter(learned_user=user).values())
        for lc in random.sample(list(learned_lc), 5):
            pro_list.append({
                "problem": {
                    "before": lc.before_kor,
                    "main": lc.cpct_kor,
                    "after": lc.after_kor
                },
                "cs": lc.cs.name
            })

        serializer = ExamSerializer(data=pro_list, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
