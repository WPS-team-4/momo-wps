from rest_framework import serializers

from post.models import PostPhoto

__all__ = (
    'PostPhotoSerializer',
)


class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        fields = (
            'pk',
            'photo',
            'post',
        )

    def to_representation(self, instance):
        ret = super(PostPhotoSerializer, self).to_representation(instance)
        ret.pop('post')
        return ret
