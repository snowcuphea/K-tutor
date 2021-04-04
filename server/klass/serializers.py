from rest_framework import serializers
from .models import Cs, Cpct, Kw, Cpcq, Lc


class CsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cs
        fields = ('name_kor', 'name_eng', 'type', 'level', 'imgurl')


class CpctSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpct
        fields = ('kor', 'eng', 'level')


class KwSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kw
        fields = ('content_kor', 'content_eng', 'count')


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
            "id", "main_kw_index", "main_kw_kor", "main_kw_eng", "main_kw_id", "meaning", "before_kor",
            "before_eng",
            "cpct_kor", "cpct_eng", "after_kor", "after_eng", "example_kor", "example_eng", "already_learned", "imgurl"
        )
