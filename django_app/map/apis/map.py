from django.db.models import Count
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from map.models import Map
from map.serializers.map import MapDetailSerializer, MapSerializer

__all__ = (
    'MapList',
    'MapDetail',
)


class MapList(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get(self, request, *args, **kwargs):

        options = request.query_params.get('opt', '')

        if options is not '':
            if 'recent_created' in options:
                queryset = Map.objects.all().order_by('-created_date')
            elif 'most_pins' in options:
                queryset = Map.objects.annotate(num_items=Count('pin')).order_by('-num_items')
        else:
            queryset = Map.objects.all().order_by('-updated_date')

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapDetailSerializer
