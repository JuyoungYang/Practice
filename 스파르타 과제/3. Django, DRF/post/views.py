from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q, F
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    게시글에 대한 CRUD 작업을 처리하는 ViewSet
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all().order_by("-created_at")

    def get_queryset(self):
        """
        검색 및 상태 필터링을 처리
        """
        queryset = super().get_queryset()
        search_query = self.request.query_params.get("search")
        status_filter = self.request.query_params.get("status")

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )

        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset

    def retrieve(self, request, *args, **kwargs):
        """
        게시글 조회 시 조회수 증가
        """
        instance = self.get_object()
        instance.view_count = F("view_count") + 1
        instance.save()
        instance.refresh_from_db()  # F() 표현식 이후 새로고침
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        liked = not user in post.likes.all()

        if liked:
            post.likes.add(user)
        else:
            post.likes.remove(user)

        return Response({"liked": liked, "total_likes": post.total_likes()})

    @action(detail=True, methods=["patch"])
    def change_status(self, request, pk=None):
        """
        게시글 상태 변경 엔드포인트
        """
        post = self.get_object()
        new_status = request.data.get("status")

        if new_status not in dict(Post.status.field.choices):
            return Response(
                {"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST
            )

        post.status = new_status
        post.save()

        return Response({"status": post.status})


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.kwargs["post_pk"], is_active=True
        ).select_related("author", "parent")

    def perform_create(self, serializer):
        """일반 댓글 생성"""
        post = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        serializer.save(post=post, author=self.request.user)

    @action(detail=True, methods=["post"])
    def replies(self, request, **kwargs):
        try:
            # 현재 댓글 객체 가져오기
            parent_comment = self.get_object()
            post = parent_comment.post

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            # 대댓글 저장
            serializer.save(post=post, author=request.user, parent=parent_comment)

            return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
