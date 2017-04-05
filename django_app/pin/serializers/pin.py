from rest_framework import serializers

from pin.models import Pin

__all__ = (
    'PinSerializer',
)


class PinSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    # place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all(),
    #                                           source='place.name')
    # map = serializers.PrimaryKeyRelatedField(queryset=Map.objects.all(),
    #                                         source='map.name')

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
