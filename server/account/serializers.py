from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ('score', 'test_at')


class AccessDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessDate
        fields = ('user', 'access_at')


class ReportSearializer(serializers.Serializer):
    user = serializers.DictField()
    learned_lc_cnt = serializers.IntegerField()
    recent_learned_lc = serializers.ListField()
    recent_lc_progress = serializers.DictField()
    progress = serializers.DictField()


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class UserAchievementSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    achievement_id = serializers.IntegerField()
    status = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()
    image = serializers.CharField()
