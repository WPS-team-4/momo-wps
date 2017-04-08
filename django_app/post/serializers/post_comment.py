from rest_framework import serializers

from post.models import PostComment

__all__ = (
    'PostCommentSerializer',
)


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'pk',
            'contents',
            'created_date',
        )