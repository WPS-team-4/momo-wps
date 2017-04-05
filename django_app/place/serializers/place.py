from rest_framework import serializers

from place.models import Place

__all__ = (
    'PlaceSerializer',
)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'pk',
            'place_id',
            'name',
            'address',
            'lat',
            'lng',
        )
