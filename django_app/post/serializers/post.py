from rest_framework import serializers

from post.models import Post
from post.serializers.post_comment import PostCommentSerializer

__all__ = (
    'PostSerializer',
    # 'PostCreateSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
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
        read_only_fields = (
            'author',
        )

