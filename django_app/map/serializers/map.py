from rest_framework import serializers

from map.models import Map

__all__ = (
    'MapSerializer',
)


class MapSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)

    class Meta:
        model = Map
        fields = (
            'pk',
            'name',
            'description',
        )
        read_only_fields = (
            'created_date',
        )
