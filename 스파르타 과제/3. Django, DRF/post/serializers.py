from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "post", "author", "content", "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at")

    def create(self, validated_data):
        # 사용자 정보는 request에서 가져옴
        user = self.context["request"].user
        validated_data["author"] = user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "author",
            "created_at",
            "updated_at",
            "comments",
            "likes_count",
            "is_liked",
        )
        read_only_fields = ("created_at", "updated_at")

    def get_likes_count(self, obj):
        return obj.total_likes()

    def get_is_liked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False
