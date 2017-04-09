from rest_framework import serializers

from pin.models import Pin

__all__ = (
    'PinSerializer',
)


class PinSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Pin
        fields = (
            'pk',
            'author',
            'name',
            'place',
            'map',
            'pin_color',
            'created_date',
        )
