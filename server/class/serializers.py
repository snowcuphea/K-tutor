from rest_framework import serializers
from .models import Cs, Cpct, Kw, Cpcq, Lc


class CsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cs
        fields = ('name', 'type', 'level')


class CpctSerializer(serializers.Modelserializer):
    class Meta:
        model = Cpct
        fields = ('kor', 'eng', 'level')


class KwSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kw
        fields = ('content', 'count')


class CpcqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpcq
        fields = ('kor', 'eng', 'kcq')


class LcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lc
        fields = '__all__'