from django.db.models import Max, Count

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


required_exp = [10, 20, 30, 50, 70,
                100, 150, 200, 250, 300,
                400, 500, 600, 750, 1000]

# 로그아웃
def logout(request):
    pass

# 회원 가입
@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# 정보 수정, 회원 탈퇴
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def account_modify_delete(request):
    # 회원 수정한 정보를 request.data에 담았다고 가정
    user = get_object_or_404(User, email=request.data['email'])
    if request.method == 'PUT':
        user.set_password(request.data['password'])
        user.save()
    elif request.method == 'DELETE':
        user.delete()
    return Response(user, status=status.HTTP_200_OK)

# 레벨업 관련
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def level_up(request):
    pass

# 업적 정보 가져오기, 업적 달성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def acheivement_list_info(request):
    pass



# # (유저의) 전체 시험 성적 조회, 등록
# @api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def result_list_create(request, user_pk):
#     user = get_object_or_404(User, pk=user_pk)
#     if request.method == 'POST':
#         TestResult.objects.create(
#             user=user,
#             score=request.data['score'],
#         )
#         data = {
#             'score': request.data['score']
#         }
#         serializer = TestResultSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         results = TestResult.objects.filter(user=user)
#         serializer = TestResultSerializer(results, many=True)
#         return Response(serializer.data)
#
# # 최고 시험 성적 조회
# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def result_max(request, user_pk):
#     user = get_object_or_404(User, pk=user_pk)
#
#     if request.method == 'GET':
#         result = TestResult.objects.aggregate(max_score=Max('score'))
#         serializer = TestResultSerializer(result)
#         return Response(serializer.data)
#
# #최근 시험 성적 조회
# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def result_latest(request, user_pk):
#     user = get_object_or_404(User, pk=user_pk)
#
#     if request.method == 'GET':
#         result = TestResult.objects.last()
#         serializer = TestResultSerializer(result)
#         return Response(serializer.data)