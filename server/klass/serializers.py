from rest_framework import serializers
from .models import Cs, Cpct, Kw, Cpcq, Lc


class CsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cs
        fields = ('name', 'type', 'level')
        example = {
            "name": "도깨비",
            "type": "drame",
            "level": 1
        }


class CpctSerializer(serializers.ModelSerializer):
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
    id = serializers.IntegerField()
    already_learned = serializers.BooleanField()
    class Meta:
        model = Lc
        fields = (
            "id", "cs_id", "main_kw_index", "main_kw_word", "main_kw_id", "meaning", "before_kor", "before_eng",
            "cpct_kor", "cpct_eng", "after_kor", "after_eng", "example", "already_learned"
        )
