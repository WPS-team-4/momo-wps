from rest_framework import serializers

from map.models import Map
from member.serializers import UserSerializer

__all__ = (
    'MapSerializer',
)


class MapSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Map
        fields = (
            'pk',
            'author',
            'name',
            'description',
        )
        read_only_fields = (
            'created_date',
        )
