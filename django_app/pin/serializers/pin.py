from rest_framework import serializers

from pin.models import Pin
from place.serializers import PlaceInfoSerializer
from post.serializers import PostSerializer
from utils import AuthorSerializer

__all__ = (
    'PinSerializer',
    'PinViewSerializer',
)


class PinSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, source='map.author')

    class Meta:
        model = Pin
        fields = (
            'pk',
            'map',
            'pin_name',
            'pin_label',
            'created_date',
            'author',
            'place',
        )
        read_only_fields = (
            'author',
        )


class PinViewSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, source='map.author')
    place = PlaceInfoSerializer(read_only=True)
    post_list = PostSerializer(read_only=True, many=True, source='post_set')

    class Meta:
        model = Pin
        fields = (
            'pk',
            'map',
            'pin_name',
            'pin_label',
            'created_date',
            'author',
            'place',
            'post_list',
        )
        read_only_fields = (
            'pk',
            'map',
            'pin_name',
            'pin_label',
            'created_date',
            'author',
            'place',
            'post_list',
        )
