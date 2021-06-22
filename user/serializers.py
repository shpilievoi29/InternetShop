from rest_framework import serializers
from django.contrib.auth.models import User
from api.permitions import UserAPIPermission, UserListAPIPermition

from user.models import Cash


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cash
        fields = "__all__"
        permission_classes = [UserListAPIPermition]


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        permissions_classes = [UserAPIPermission]

