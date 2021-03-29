import operator
from functools import reduce

from django.http import Http404
from django.views import View
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .data_update import *
from .serializers import *

from account.models import Recent_learned_lc
from django.db.models import Q


@api_view(['GET'])
def updateDB(request):
    # update()
    # create_lc()
    add_meaning_to_lc()
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
    authentication_classes = JSONWebTokenAuthentication
    permission_classes = IsAuthenticated

    def get_queryset(self):
        conditions = {
            'id': self.kwargs.get("music_num", None),
        }
        conditions = {key: val for key, val in conditions.items() if val is not None}

        lc = Lc.objects.filter(**conditions)
        if not lc.exists():
            raise Http404()
        return lc

    def get(self, request, type, title):
        if type != 'kpop':
            cs = get_object_or_404(Cs, name=title)
            lcs = list(Lc.objects.filter(cs=cs).values())
        else:
            css = Cs.objects.filter(name__contains=title)
            lcs = list(Lc.objects.filter(cs__in=css).values())
        user = request.user
        lcs_dict = [lc.__dict__ for lc in lcs]
        for lc in lcs_dict:
            lc['already_learned'] = True if Lc.objects.filter(Q(learned_user=user) | Q(id=lc.id)).exists() else False

        serializer = LcSerializer(data=lcs_dict, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LcViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                View):
    serializer_class = LcSerializer
    authentication_classes = JSONWebTokenAuthentication
    permission_classes = IsAuthenticated

    def get_queryset(self):
        conditions = {
            'id': self.kwargs.get("music_num", None),
        }
        conditions = {key: val for key, val in conditions.items() if val is not None}

        lc = Lc.objects.filter(**conditions)
        if not lc.exists():
            raise Http404()

        return lc

    def get(self, request, LcId):
        lc = get_object_or_404(Lc, id=LcId)
        serializer = LcSerializer(lc)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def done(self, request, LcId):
        user = request.user
        lc = get_object_or_404(Lc, id=LcId)
        user.learned_lc.add(lc)
        user.save()
        Recent_learned_lc.objects.create(user=user, lc=lc)
        return Response("ok", status=status.HTTP_200_OK)
