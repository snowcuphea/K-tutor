from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'nickname', 'level', 'exp', 'consecutive_access')


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ('score', 'test_at')


class AccessDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessDate
        fields = ('user', 'access_at')


class ReportSearializer(serializers.Serializer):
    user = serializers.DictField
    consecutive_access_date = serializers.IntegerField()
    learned_lc_cnt = serializers.IntegerField()
    recent_learned_lc = serializers.ListField()
    recent_lc_progress = serializers.DictField()
    progress = serializers.DictField()

# class AchievementSerializer(serializers.Modelserializer):
#     class Meta:
#         model = Acheivement
#         fields = ('title', 'content', 'image_on', 'image_off')
