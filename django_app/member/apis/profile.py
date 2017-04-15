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

    def retrieve(self, request, *args, **kwargs):
        user = MomoUser.objects.get(pk=kwargs['pk'])
        fields = request.query_params.get('fields', '')
        if fields is not '':
            fields = fields.split(',')
        else:
            fields = None
        serializer = UserSerializer(user, fields=fields)
        return Response(serializer.data)
