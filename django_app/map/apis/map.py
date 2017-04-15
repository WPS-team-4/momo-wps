from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response

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

    def get(self, request, *args, **kwargs):
        if self.request.auth:
            fields = request.query_params.get('fields', '')
            if fields is not '':
                fields = fields.split(',')
                if 'recent_updated' in fields:
                    queryset = Map.objects.all().order_by('-created_date')
            else:
                queryset = Map.objects.filter(author=self.request.user)

            # page = self.paginate_queryset(queryset)
            # if page is not None:
            #     serializer = self.get_serializer(page, many=True)
            #     return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            raise NotAuthenticated


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapDetailSerializer
