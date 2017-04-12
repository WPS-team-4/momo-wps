from rest_framework import serializers

from pin.models import Pin
from post.serializers import PostSerializer

__all__ = (
    'PinSerializer',
)


class PinSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post_list = PostSerializer(read_only=True, many=True, source='post_set')

    class Meta:
        model = Pin
        fields = (
            'pk',
            'author',
            'name',
            'place',
            'map',
            'pin_color',
            'created_date',
            'post_list',
        )
