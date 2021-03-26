from rest_framework import serializers
from .models import Acheivement

class AcheivementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acheivement
        fields = ('id', 'title', 'content', 'username', 'created_at', 'updated_at')