from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email"]
