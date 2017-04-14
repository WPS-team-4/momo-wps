from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from member.models import MomoUser
from member.serializers import UserSerializer
from utils import IsOwnerOrReadOnly

__all__ = (
    'UserProfileViewAPI',
)


class UserProfileViewAPI(RetrieveUpdateAPIView):
    queryset = MomoUser.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     user = request.user
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

        # def partial_update(self, request, *args, **kwargs):
        #     partial = kwargs.pop('partial', True)
        #     instance = request.user
        #     serializer = UserSerializer(instance, data=request.data, partial=partial)
        #     return Response(serializer.data)
