from django.db.models import Count
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
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
        try:
            user = MomoUser.objects.get(pk=kwargs['pk'])
            fields = request.query_params.get('fields', '')
            if fields is not '':
                fields = fields.split(',')
            else:
                fields = None
            serializer = UserSerializer(user, fields=fields)
            return Response(serializer.data)
        except MomoUser.DoesNotExist:
            raise Http404("해당 pk의 user가 존재하지 않습니다.")


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
                queryset = MomoUser.objects.annotate(count_follower=Count('relation_to_user')).order_by(
                    '-count_follower')
            elif 'most_maps' in options:
                queryset = MomoUser.objects.annotate(count_maps=Count('map')).order_by('-count_maps')
            else:
                raise ValidationError(detail="opt 값을 정확히 입력해 주세요.")
        else:
            queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, fields=fields, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
