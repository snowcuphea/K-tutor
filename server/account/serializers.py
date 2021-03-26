from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import TestResult, AccessDate

User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
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