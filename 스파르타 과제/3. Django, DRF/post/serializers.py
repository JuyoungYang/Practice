from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    """
    댓글 모델을 위한 시리얼라이저.
    댓글 작성자 정보, 내용, 생성 및 수정 시간을 포함합니다.
    """

    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "content",
            "created_at",
            "updated_at",
            "parent",
            "replies",
            "is_active",
        )
        read_only_fields = ("id", "author", "created_at", "updated_at")

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.filter(is_active=True), many=True).data
        return []


class PostSerializer(serializers.ModelSerializer):
    """
    게시글 모델을 위한 시리얼라이저.
    게시글 정보, 작성자 정보, 댓글 목록, 좋아요 수, 현재 사용자의 좋아요 여부를 포함합니다.
    """

    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(source="total_likes", read_only=True)
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
            "status",
            "view_count",
        )
        read_only_fields = (
            "id",
            "author",
            "created_at",
            "updated_at",
            "likes_count",
            "view_count",
        )

    def get_is_liked(self, obj):
        """
        현재 요청 사용자가 이 게시글에 좋아요를 눌렀는지 여부를 반환합니다.
        """
        request = self.context.get("request")
        return (
            request
            and request.user.is_authenticated
            and obj.likes.filter(id=request.user.id).exists()
        )
