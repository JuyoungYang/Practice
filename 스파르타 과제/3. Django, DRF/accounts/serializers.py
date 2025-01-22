from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    기본 사용자 정보 시리얼라이저
    """

    class Meta:
        model = User
        fields = ("id", "username", "email", "profile_image", "bio", "created_at")
        read_only_fields = ("id", "created_at")


class UserDetailSerializer(UserSerializer):
    """
    상세 사용자 정보 시리얼라이저
    """

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ("updated_at",)
        read_only_fields = ("id", "created_at", "updated_at")


class RegisterSerializer(serializers.ModelSerializer):
    """
    회원가입을 위한 시리얼라이저
    """

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2", "email", "profile_image", "bio")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    JWT 토큰 커스텀 시리얼라이저
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        data["email"] = self.user.email
        return data


class ChangePasswordSerializer(serializers.Serializer):
    """
    비밀번호 변경을 위한 시리얼라이저
    """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
