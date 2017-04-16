from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from member.models import MomoUser
from member.serializers import UserSerializer
from utils import IsOwnerOrReadOnly

__all__ = (
    'UserDetailAPI',
    'UserAPI',
)


class UserDetailAPI(RetrieveUpdateAPIView):
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


class UserAPI(RetrieveAPIView):
    queryset = MomoUser.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        fields = request.query_params.get('fields', '')
        options = request.query_params.get('opt', '')
        if fields is not '':
            fields = fields.split(',')
        else:
            fields = None

        if options is not '':
            if 'most_follower' in options:
                queryset = MomoUser.objects.filter()
            elif 'most_maps' in options:
                queryset = MomoUser.objects.extra(
                    select={
                        'count_maps': 'SELECT COUNT(*) FROM map_map WHERE map_map.author_id = member_momouser.id'
                    },
                ).extra(order_by=['-count_maps'])
        else:
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, fields=fields, many=True)
        return Response(serializer.data)
