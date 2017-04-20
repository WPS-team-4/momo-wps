from rest_framework import serializers

from map.models import Map
from member.models import MomoUser
from pin.serializers.pin import PinViewSerializer

__all__ = (
    'MapUserSerializer',
    'MapSerializer',
    'MapDetailSerializer',
)


class MapUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'profile_img',
        )


class MapSerializer(serializers.ModelSerializer):
    author = MapUserSerializer(read_only=True)
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
    author = MapUserSerializer(read_only=True)
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