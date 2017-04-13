<<<<<<< HEAD
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from member.models import MomoUser
from member.serializers import UserSerializer
=======
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from member.models import MomoUser
from member.serializers import UserSerializer
from member.serializers.profile import UserProfileSerializer
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

__all__ = (
    'UserProfileViewAPI',
)


class UserProfileViewAPI(RetrieveUpdateAPIView):
    queryset = MomoUser.objects.all()
    permission_classes = (IsAuthenticated,)
<<<<<<< HEAD
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = UserSerializer
=======
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserProfileSerializer
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

    def retirieve(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = request.user
        serializer = UserSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
