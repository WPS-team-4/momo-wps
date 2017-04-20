from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        data = request.data
        if len(data) >= 2:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
        return response

    def perform_create(self, serializer):
        serializer.save()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

