from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    role_display = serializers.CharField(
        source="get_role_display",
        read_only=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "role",
            "role_display",
        ]


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "phone_number",
            "role",
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)