from rest_framework import serializers

from map.models import Map
from pin.serializers import PinSerializer

__all__ = (
    'MapSerializer',
    'MapDetailSerializer',
)


class MapSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Map
        fields = (
            'pk',
            'map_name',
            'description',
            'is_private',
            'author',
            'created_date',
        )


class MapDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    pin_list = PinSerializer(read_only=True, many=True, source='pin_set')

    class Meta:
        model = Map
        fields = (
            'pk',
            'map_name',
            'description',
            'author',
            'pin_list',
            'created_date',
            'is_private',
        )
