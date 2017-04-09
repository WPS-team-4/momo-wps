from rest_framework import generics

from post.models import PostComment
from post.serializers import PostCommentSerializer


class PostCommentCreate(generics.CreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
        )


class PostCommentDestroy(generics.DestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
