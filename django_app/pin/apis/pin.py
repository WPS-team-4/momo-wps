import requests
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from config.settings import config
from pin.models import Pin
from pin.serializers.pin import PinSerializer
from place.models import Place

__all__ = (
    'PinList',
    'PinDetail',
)


class PinList(generics.ListCreateAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        data = request.data
        pin_data = data['pin']
        place_data = data['place']

        place = self.place_data_to_object(place_data)
        data = {
            'place': place,
        }
        data.update(pin_data)

        serializer = PinSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def place_data_to_object(self, data):
        # place data에 모든 데이터가 들어있는 경우
        # serializer = PlaceSerializer(data=data)
        # serializer.is_valid()

        # place에  latlng만 있는 경우
        lat = data['lat']
        lng = data['lng']
        url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        params = {
            'key': config['google_geocoding_api']['key'],
            'latlng': '{},{}'.format(lat, lng)
        }
        search_result = requests.get(url, params=params).json()
        reverse_geo_data = search_result['results'][0]
        place_id = reverse_geo_data['place_id']
        address = reverse_geo_data['formatted_address']
        defaults = {
            'name': 'marking',
            'address': address,
            'lat': lat,
            'lng': lng
        }
        place, _ = Place.objects.get_or_create(place_id=place_id, defaults=defaults)
        place_pk = place.id
        return place_pk


class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
