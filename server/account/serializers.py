from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializers(serializers.Modelserializers):
    class Meta:
        model = User
        fields = ('username', 'password')