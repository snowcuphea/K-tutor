from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import TestResult, AccessDate

User = get_user_model()

class UserSerializer(serializers.Modelserializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'level', 'exp')

class TestResultSerializer(serializers.Modelserializer):
    class Meta:
        model = TestResult
        fields = ('score', 'test_at')

class AccessDateSerializer(serializers.Modelserializer):
    class Meta:
        model = AccessDate
        fields = ('access_at')


class ReportSearializer(serializers.Serializer):
    consecutive_access_date = serializers.IntegerField()
    learned_lc_cnt = serializers.IntegerField()
    recent_learned_lc = serializers.ListField()
    recent_lc_progress = serializers.DictField()
    progress = serializers.DictField()
