from rest_framework import serializers

from pin.models import Pin
<<<<<<< HEAD
=======
from post.serializers import PostSerializer
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

__all__ = (
    'PinSerializer',
)


class PinSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
<<<<<<< HEAD
=======
    post_list = PostSerializer(read_only=True, many=True, source='post_set')
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

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
<<<<<<< HEAD
=======
            'post_list',
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
        )
