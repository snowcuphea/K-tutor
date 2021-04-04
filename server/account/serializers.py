from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'level', 'exp')


class AccessDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessDate
        fields = ('user', 'access_at')


class ReportSearializer(serializers.Serializer):
    user = serializers.DictField()
    learned_lc_cnt = serializers.IntegerField()
    recent_learned_lc = serializers.ListField()
    recent_lc_progress = serializers.DictField()
    recent_cs = serializers.DictField()
    progress = serializers.DictField()


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'title', 'imgurl')


class AchievedManageSerializer(serializers.Serializer):
    achievement_id = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()
    imgurl = serializers.CharField()
    done = serializers.IntegerField()
    total = serializers.IntegerField()
    status = serializers.IntegerField()
    great_kor = serializers.CharField()
    great_eng = serializers.CharField()
    great_dsc = serializers.TextField()
