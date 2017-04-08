from rest_framework import serializers

from post.models import Post
from post.serializers.post_comment import PostCommentSerializer
from post.serializers.post_photo import PostPhotoSerializer

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    pin = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    photo_list = PostPhotoSerializer(read_only=True, many=True, source='postphoto_set')
    comment_list = PostCommentSerializer(read_only=True, many=True, source='postcomment_set')

    class Meta:
        model = Post
        fields = (
            'pk',
            'pin',
            'author',
            'created_date',
            'photo_list',
            'comment_list',
        )