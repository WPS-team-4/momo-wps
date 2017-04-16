from rest_framework import serializers

from pin.models import Pin
from place.serializers import PlaceSerializer
from post.serializers import PostSerializer

__all__ = (
    'PinSerializer',
    'PinCreateSerializer',
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
            # 'pk',
            'author',
            'post_list',
            'place',
        )


class PinCreateSerializer(serializers.Serializer):
    pin = PinSerializer()
    place = PlaceSerializer()
