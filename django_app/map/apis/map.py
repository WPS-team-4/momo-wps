from django.db.models import Count
from django.http import Http404
from rest_framework import generics
from rest_framework.exceptions import ValidationError
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
                raise ValidationError(detail="opt 값을 정확히 입력해 주세요.")
        else:
            queryset = Map.objects.all().order_by('-updated_date')

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            map = Map.objects.get(pk=kwargs['pk'])
            serializer = MapDetailSerializer(map)
            return Response(serializer.data)
        except Map.DoesNotExist:
            raise Http404("해당 pk의 지도가 존재하지 않습니다")
