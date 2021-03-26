from rest_framework import serializers
from .models import Cs, Cpct, Kw, Cpcq


class CsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cs
        fields = ('name', 'type', 'level')


class CpctSerializers(serializers.Modelserializer):
    class Meta:
        model = Cpct
        fields = ('kor', 'eng', 'level')


class KwSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kw
        fields = ('content', 'count')


class CpcqSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cpcq
        fields = ('kor', 'eng', 'kcq')
