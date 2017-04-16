from rest_framework import generics
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from map.models import Map
from map.serializers.map import MapDetailSerializer

__all__ = (
    'MapList',
    'MapDetail',
)


class MapList(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get(self, request, *args, **kwargs):
        try:
            fields = request.query_params.get('fields', '')
            if fields is not '':
                fields = fields.split(',')
                if 'recent_updated' in fields:
                    queryset = Map.objects.all().order_by('-created_date')
                elif 'recent_created' in fields:
                    queryset = Map.objects.all().order_by('-created_date')
                elif 'most_pins' in fields:
                    queryset = Map.objects.extra(
                        select={
                            'count_pins': 'SELECT COUNT(*) FROM pin_pin WHERE pin_pin.map_id = map_map.id'
                        },
                    ).extra(order_by=['-count_pins'])

            else:
                queryset = Map.objects.filter(author=self.request.user)

            # page = self.paginate_queryset(queryset)
            # if page is not None:
            #     serializer = self.get_serializer(page, many=True)
            #     return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except TypeError:
            raise NotAuthenticated(detail='로그인 해주세요')


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapDetailSerializer
