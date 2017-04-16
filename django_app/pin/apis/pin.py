from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from map.models import Map
from pin.models import Pin
from pin.serializers.pin import PinSerializer, PinCreateSerializer
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
        serializer = PinCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        place_data = data['place']
        pin_data = data['pin']
        place = self.place_data_to_object(place_data)
        pin = self.create_pin_object(pin_data, place)
        serializer = PinSerializer(pin)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def place_data_to_object(self, data):
        # place = Place.objects.create(
        #     place_id=data['place_id'],
        #     name=data['name'],
        #     address=data['address'],
        #     lat=data['lat'],
        #     lng=data['lng']
        # )
        defaults = {
            'name': data['name'],
            'address': data['address'],
            'lat': data['lat'],
            'lng': data['lng'],
        }
        place, _ = Place.objects.get_or_create(place_id=data['place_id'], defaults=defaults)
        return place

    def create_pin_object(self, data, place):
        map = Map.objects.get(pk=data['map'])
        pin = Pin.objects.create(
            place=place,
            map=map,
            pin_name=data['pin_name'],
            pin_color=data['pin_color']
        )
        return pin


class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
