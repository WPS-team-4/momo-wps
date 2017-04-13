from rest_framework import serializers

from pin.models import Pin
from post.serializers import PostSerializer

__all__ = (
    'PinSerializer',
)


class PinSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        source='map.author',
        slug_field='username',
        read_only=True
    )
    post_list = PostSerializer(read_only=True, many=True, source='post_set')

    class Meta:
        model = Pin
        fields = (
            'pk',
            'author',
            'map',
            'pin_name',
            'place',
            'pin_color',
            'created_date',
            'post_list',
        )
        read_only_fields = (
            'author',
        )
