from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from post.models import Post
from utils import AuthorSerializer

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, source='pin.map.author')
    photo = VersatileImageFieldSerializer(sizes='post', required=False)

    class Meta:
        model = Post
        fields = (
            'pk',
            'pin',
            'author',
            'photo',
            'description',
            'created_date',
        )
