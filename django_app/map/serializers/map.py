from rest_framework import serializers

from pin.serializers import PinSerializer
from map.models import Map

__all__ = (
    'MapSerializer',
)


class MapSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    pin_list = PinSerializer(read_only=True, many=True, source='pin_set')

    class Meta:
        model = Map
        fields = (
            'pk',
            'name',
            'description',
            'pin_list',
        )
        read_only_fields = (
            'created_date',
            'is_private',
            'is_visible',
        )
