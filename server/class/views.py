from django.views import View
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .data_update import *
from .serializers import *


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
        Cs = Cs.objects.filter(**conditions)
        if not Cs.exists():
            raise Http404()
        return Cs



    def cs_list(self, request, type):
        if type == 'kpop':
            song_list = Cs.objects.filter(cs="kpop")
            cs_list_temp = list(set({x.name.split(" - ")[0] for x in song_list}))
            cs_list = []
            for cs in cs_list_temp:
                cs_list.append({
                    "name": cs,
                    "type": "kpop",
                    "level": song_list.filter(name__contains=cs)[0].level
                })
        else:
            cs_list = Cs.objects.filter(type=type)
        serializer = CsSerializer(data=cs_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LcListViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                View):
    serializer_class = LcSerializer


    def get_queryset(self):
    	conditions = {
            'id': self.kwargs.get("music_num", None),
        }
        conditions = {key: val for key, val in conditions.items() if val is not None}

        Lc = Lc.objects.filter(**conditions)
        if not Lc.exists():
            raise Http404()

        return Cs


    def list(self, request, type, title):
        if type != 'kpop':
            cs = get_object_or_404(Cs, name=title)
            lcs = Lc.objects.filter(cs=cs)
            serializer = LcSerializer(data=lcs, many=True)
        else:
            css = Cs.objects.filter(name__contains=title)
            lcs = Lc.objects.filter(cs__in=css)
            serializers = LcSerializer(data=lcs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LcViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                View):
    serializer_class = LcSerializer


    def get_queryset(self):
    	conditions = {
            'id': self.kwargs.get("music_num", None),
        }
        conditions = {key: val for key, val in conditions.items() if val is not None}

        Lc = Lc.objects.filter(**conditions)
        if not Lc.exists():
            raise Http404()

        return Lc


    def get(self, LcId):
        lc = get_object_or_404(Lc, id=LcId)
        serializers = LcSerializer(lc)
        return Response(serializers.data, status=status.HTTP_200_OK)
