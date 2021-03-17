from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers, User

from django.shortcuts import get_object_or_404

@api_view(['PUT', 'DELETE'])
def account_modify_delete(request):
    # 회원 수정한 정보를 request.data에 담았다고 가정
    user = get_object_or_404(User, username=request.data['username'])
    if request.method == 'PUT':
        user.set_password(request.data['password'])
        user.save()
    elif request.method == 'DELETE':
        user.delete()
    return Response(user, status=status.HTTP_200_OK)