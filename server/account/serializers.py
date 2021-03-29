from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Modelserializer):
    class Meta:
        model = User
        fields = ('user_id', 'email', 'password', 'nickname', 'level', 'exp', 'consecutive_access')


# class AccessDateSerializer(serializers.Modelserializer):
#     class Meta:
#         model = AccessDate
#         fields = ('user', 'access_at')
#
#
# class AchievementSerializer(serializers.Modelserializer):
#     class Meta:
#         model = Acheivement
#         fields = ('title', 'content', 'image_on', 'image_off')
