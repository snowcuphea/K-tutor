from rest_framework import serializers
from .models import *


class ExamResultSerializer(serializers.ModelSerializer):
    exam_date = serializers.DateTimeField()
    class Meta:
        model = ExamResult
        fields = ('score', 'exam_date')


class ExamSerializer(serializers.Serializer):
    problem = serializers.DictField()
    cs = serializers.CharField(max_length=100)

    class Meta:
        fields = '__all__'
