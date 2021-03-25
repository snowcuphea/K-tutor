from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .data_update import *
from .serializers import *


@api_view(['GET'])
def updateDB(request):
    # update()
    create_lc()
    return Response("OK", status=status.HTTP_200_OK)

@api_view(['GET'])
def cs_list(request, type):
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
