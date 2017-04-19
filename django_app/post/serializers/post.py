from rest_framework import serializers

from post.models import Post

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        source='pin.map.author',
        slug_field='username',
        read_only=True
    )

    # comment_list = PostCommentSerializer(read_only=True, many=True, source='postcomment_set')

    class Meta:
        model = Post
        fields = (
            'pk',
            'pin',
            'author',
            'photo',
            'created_date',
            'description',
        )
        read_only_fields = (
            'author',
            'photo',
            'description',
        )
