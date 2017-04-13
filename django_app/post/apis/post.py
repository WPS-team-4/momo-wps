from rest_framework import generics
from rest_framework import permissions

from post.models import Post
from post.serializers.post import PostSerializer

__all__ = (
    'PostList',
    'PostDetail',
)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

