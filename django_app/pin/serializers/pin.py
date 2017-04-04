from rest_framework import serializers

from member.serializers import UserSerializer
from pin.models import Pin

__all__ = (
    'PinSerializer'
)


class PinSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Pin
        fields = (
            'pk',
            'author',
            'place',
            'map'
        )
