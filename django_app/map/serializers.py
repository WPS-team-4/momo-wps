from rest_framework import serializers

from map.models import Map


# from member.serializers import UserSerializer


class MapSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Map
        fields = (
            'pk',
            'name',
            'description',
            'created_date',
            'is_private',
            'is_visible'
        )
