from rest_framework import generics

from post.models import PostComment
from post.serializers import PostCommentSerializer


class PostCommentCreate(generics.CreateAPIView):
    serializer_class = PostCommentSerializer

    def get_queryset(self):
        queryset = PostComment.objects.all()
        post = self.kwargs['post_id']
        queryset = queryset.filter(postcomment__post=post)
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
        )


class PostCommentDestroy(generics.DestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
