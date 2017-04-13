from rest_framework import serializers

from map.models import Map
<<<<<<< HEAD
from member.serializers import UserSerializer
=======
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
from pin.serializers import PinSerializer

__all__ = (
    'MapSerializer',
    'MapDetailSerializer',
)


class MapSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    author = UserSerializer(read_only=True)
=======
    # author = UserSerializer(read_only=True)
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

    class Meta:
        model = Map
        fields = (
            'pk',
            'name',
            'description',
            'is_private',
<<<<<<< HEAD
            'author',
=======
            # 'author',
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
            'created_date',
        )


class MapDetailSerializer(serializers.ModelSerializer):
    pin_list = PinSerializer(read_only=True, many=True, source='pin_set')
<<<<<<< HEAD
    author = UserSerializer(read_only=True)
=======

    # author = UserSerializer(read_only=True)
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

    class Meta:
        model = Map
        fields = (
            'pk',
            'name',
            'description',
<<<<<<< HEAD
            'author',
=======
            # 'author',
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
            'pin_list',
            'created_date',
            'is_private',
        )
