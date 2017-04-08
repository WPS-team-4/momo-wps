from rest_framework import generics

from post.models import PostComment
from post.serializers import PostCommentSerializer


class PostCommentCreate(generics.CreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer


class PostCommentDestroy(generics.DestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
