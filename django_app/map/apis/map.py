from rest_framework import generics
from rest_framework import permissions

from map.models import Map
from map.serializers import MapSerializer
from map.serializers.map import MapDetailSerializer

__all__ = (
    'MapList',
    'MapDetail',
)


class MapList(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapDetailSerializer


