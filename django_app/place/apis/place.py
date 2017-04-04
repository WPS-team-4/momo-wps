from rest_framework import generics

from place.models import Place
from place.serializers.place import PlaceSerializer

__all__ = (
    'PlaceList',
    'PlaceDetail',
)


class PlaceList(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def perform_create(self, serializer):
        serializer.save()


class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
