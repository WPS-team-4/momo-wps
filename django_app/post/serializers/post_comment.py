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
            'post',
            'contents',
            'author',
        )

    def to_representation(self, instance):
        ret = super(PostCommentSerializer, self).to_representation(instance)
        ret.pop('post')
        return ret
