from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

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
    photo = VersatileImageFieldSerializer(sizes='post')

    class Meta:
        model = Post
        fields = (
            'pk',
            'pin',
            'author',
            'photo',
            'description',
            'created_date',
        )
        read_only_fields = (
            'author',
        )
