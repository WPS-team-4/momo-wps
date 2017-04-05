from rest_framework import serializers

from map.models import Map
from member.serializers import UserSerializer
from pin.models import Pin
from place.models import Place

__all__ = (
    'PinSerializer'
)


class PinSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    # place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all(),
    #                                            source='place.name')
    # map = serializers.PrimaryKeyRelatedField(queryset=Map.objects.all(),
    #                                          source='map.name')

    class Meta:
        model = Pin
        fields = (
            'pk',
            'author',
            'name',
            'place',
            'map',
            'pin_color',
            'is_private',
        )
        read_only_fields = (
            'created_date',
            'is_visible',
        )
