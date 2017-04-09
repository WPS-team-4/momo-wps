from rest_framework import serializers

from pin.models import Pin
from post.models import Post
from post.serializers.post_comment import PostCommentSerializer

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    pin = serializers.PrimaryKeyRelatedField(queryset=Pin.objects.all(), source='pin.name')
    comment_list = PostCommentSerializer(read_only=True, many=True, source='postcomment_set')

    class Meta:
        model = Post
        fields = (
            'pk',
            'pin',
            'author',
            'photo',
            'created_date',
            'comment_list',
        )
