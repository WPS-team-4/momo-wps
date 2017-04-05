from rest_framework import generics
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from pin.models import Pin
from pin.serializers.pin import PinSerializer

__all__ = (
    'PinList',
    'PinDetail',
)


class PinList(generics.ListCreateAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)


