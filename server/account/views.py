from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers

@api_view(['PUT'])
def account_modify(request):
    # 회원 수정한 정보를 request.data에 담았다고 가정
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def account_delete(request):
    serializer = UserSerializers(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user.delete()

    return Response(serializer.data, status=status.HTTP_200_OK)