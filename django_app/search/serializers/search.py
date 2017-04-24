from rest_framework import serializers

from map.serializers import MapSerializer
from utils import AuthorSerializer

__all__ = (
    'SearchResultSerializer',
)


class SearchResultSerializer(serializers.Serializer):
    maps = serializers.ListField(child=MapSerializer())
    users = serializers.ListField(child=AuthorSerializer())
