from rest_framework import generics

from post.models import Post
from post.serializers.post import PostSerializer

__all__ = (
    'PostList',
    'PostDetail'

)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
