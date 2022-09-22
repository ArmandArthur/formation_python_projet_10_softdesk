from rest_framework import serializers
from users.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = (serializers.EmailField(max_length=255, min_length=4),)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("Email is already in use")})
        return super().validate(attrs)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]
