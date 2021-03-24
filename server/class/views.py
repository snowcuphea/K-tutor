from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .data_update import *


@api_view(['GET'])
def updateDB(request):
    # update()
    create_lc()
    return Response("OK", status=status.HTTP_200_OK)


def cs_list(request, type):
    return
