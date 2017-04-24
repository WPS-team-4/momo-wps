from rest_framework import serializers

from map.models import Map
from pin.serializers.pin import PinViewSerializer
from utils import AuthorSerializer

__all__ = (
    'MapSerializer',
    'MapDetailSerializer',
)


class MapSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    pin_list = PinViewSerializer(read_only=True, many=True, source='pin_set')

    class Meta:
        model = Map
        fields = (
            'pk',
            'author',
            'map_name',
            'description',
            'created_date',
            'is_private',
            'pin_list'
        )


class MapDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    pin_list = PinViewSerializer(read_only=True, many=True, source='pin_set')

    class Meta:
        model = Map
        fields = (
            'pk',
            'author',
            'map_name',
            'description',
            'created_date',
            'is_private',
            'pin_list'
        )
