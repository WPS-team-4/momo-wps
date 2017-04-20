from rest_framework import serializers

from pin.models import Pin
from place.serializers import PlaceSerializer
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
    place = PlaceSerializer(read_only=True)

    class Meta:
        model = Pin
        fields = (
            'pk',
            'map',
            'pin_name',
            'pin_color',
            'created_date',
            'author',
            'place',
            'post_list',

        )
        read_only_fields = (
            'author',
            'post_list',
        )
