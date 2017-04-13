from rest_framework import generics
from rest_framework import permissions

from rest_framework import status
from rest_framework.response import Response

from post.models import Post
from post.serializers.post import PostSerializer, PostCreateSerializer

__all__ = (
    'PostList',
    'PostDetail',
)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        # self.request.data['author'] = self.request.user
        serializer = PostCreateSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'post created'}, status=status.HTTP_201_CREATED)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
