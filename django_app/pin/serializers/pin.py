from rest_framework import serializers

from pin.models import Pin
from post.serializers import PostSerializer

__all__ = (
    'PinSerializer',
)


class PinSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        source='map.author',
        slug_field='username',
        read_only=True
    )
    # author = UserSerializer(read_only=True, source='map__author')
    # author = serializers.SlugRelatedField(
    #     slug_field='username',
    #     source='map__author',
    #     read_only=True,
    # )
    # author = serializers.PrimaryKeyRelatedField(
    #     source='map.author',
    #     read_only=True,
    # )

    post_list = PostSerializer(read_only=True, many=True, source='post_set')

    class Meta:
        model = Pin
        fields = (
            'pk',
            'author',
            'map',
            'name',
            'place',
            'map',
            'pin_color',
            'created_date',
            'post_list',
        )
