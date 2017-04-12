from rest_framework import serializers

from post.models import PostComment

__all__ = (
    'PostCommentSerializer',
)


class PostCommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = PostComment
        fields = (
            'pk',
            'post',
            'contents',
            'author',
        )

    def to_representation(self, instance):
        ret = super(PostCommentSerializer, self).to_representation(instance)
        ret.pop('post')
        return ret
