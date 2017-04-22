from rest_framework import serializers

from place.models import Place

__all__ = (
    'PlaceSerializer',
    'PlaceInfoSerializer',
)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'pk',
            'googlepid',
            'name',
            'address',
            'lat',
            'lng',
        )


class PlaceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'pk',
            'address',
            'lat',
            'lng',
        )
