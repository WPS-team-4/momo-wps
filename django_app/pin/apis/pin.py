import requests
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from config.settings import config
from pin.models import Pin
from pin.serializers.pin import PinSerializer, PinViewSerializer
from place.models import Place
from place.serializers import PlaceSerializer

__all__ = (
    'PinList',
    'PinDetail',
)


class PinList(generics.ListCreateAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PinViewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PinViewSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        pin_data = data['pin']
        place_data = data['place']

        if 'place_id' in place_data:
            googlepid = place_data['place_id']

            # place_id 를 갖는 객체가 DB에 있으면 가져오고
            if Place.objects.filter(googlepid=googlepid).exists():
                place = Place.objects.get(googlepid=googlepid)

            # 없으면 생성한다
            else:
                place_data['googlepid'] = place_data.pop('place_id')
                serializer = PlaceSerializer(data=place_data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                place = serializer.validated_data
        else:
            # place_id 가 place_data에 없으면 place_data_to_object실행
            place = self.latlng_to_object(data=place_data)

        data = {
            "place": str(place.pk)
        }
        data.update(pin_data)
        serializer = PinSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        pin = serializer.save()
        headers = self.get_success_headers(serializer.data)

        result = PinViewSerializer(pin)
        return Response(result.data, status=status.HTTP_201_CREATED, headers=headers)

    def latlng_to_object(self, data):
        # data에 latlng만 있는 경우
        API_KEY = config['google_geocoding_api']['key']
        lat = data['lat']
        lng = data['lng']
        url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        params = {
            'key': API_KEY,
            'latlng': '{},{}'.format(lat, lng)
        }
        search_result = requests.get(url, params=params).json()
        reverse_geo_data = search_result['results'][0]
        place_id = reverse_geo_data['place_id']
        address = reverse_geo_data['formatted_address']
        defaults = {
            'googlepid': place_id,
            'name': 'marking',
            'address': address,
            'lat': lat,
            'lng': lng,
        }
        place, _ = Place.objects.get_or_create(googlepid=place_id, defaults=defaults)
        return place


class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PinViewSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        pin = serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        result = PinViewSerializer(pin)
        return Response(result.data)
