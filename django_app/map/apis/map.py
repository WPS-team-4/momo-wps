from rest_framework import generics
from rest_framework import permissions
<<<<<<< HEAD
=======
from rest_framework.response import Response
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

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

<<<<<<< HEAD
=======
    def get(self, request, *args, **kwargs):
        queryset = Map.objects.filter(author=self.request.user)
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapDetailSerializer
<<<<<<< HEAD


=======
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
