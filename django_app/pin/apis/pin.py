from rest_framework import generics
from rest_framework import permissions
<<<<<<< HEAD
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
=======
from rest_framework.authentication import TokenAuthentication
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

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
<<<<<<< HEAD
    authentication_classes = (JSONWebTokenAuthentication,)
=======
    authentication_classes = (TokenAuthentication,)
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
<<<<<<< HEAD
    authentication_classes = (JSONWebTokenAuthentication,)


=======
    authentication_classes = (TokenAuthentication,)
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
