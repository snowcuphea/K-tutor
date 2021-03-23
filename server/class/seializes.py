from rest_framework import serializers
from .models import Cs, Cpct, Kw


class CsSerializers(serializers.Modelserializers):
    class Meta:
        model = Cs
        fields = ('title', 'type', 'level')


class CpctSerializers(serializers.Modelserializers):
    class Meta:
        model = Cpct
        fields = ('kor', 'eng', 'level')


class KwSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kw
        fields = ('content', 'count')
