from rest_framework import serializers

from map.models import Map
from member.serializers import UserSerializer
from pin.serializers import PinSerializer

__all__ = (
    'MapSerializer',
    'MapDetailSerializer',
)


class MapSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Map
        fields = (
            'pk',
            'name',
            'description',
            'is_private',
            'author',
            'created_date',
        )


class MapDetailSerializer(serializers.ModelSerializer):
    pin_list = PinSerializer(read_only=True, many=True, source='pin_set')
    author = UserSerializer(read_only=True)

    class Meta:
        model = Map
        fields = (
            'pk',
            'name',
            'description',
            'author',
            'pin_list',
            'created_date',
            'is_private',
        )
