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
            'author',
            'map_name',
            'description',
            'is_private',
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
            'author',
            'map_name',
            'description',
            'pin_list',
            'is_private',
            'created_date',

        )
