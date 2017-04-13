from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import RelationShip, MomoUser
from member.serializers import RelationShipSerializer

__all__ = (
    'FollowAPI',
)


class FollowAPI(APIView):
    serializer_class = RelationShipSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        from_user = MomoUser.objects.get(id=self.kwargs['pk'])
        relation, is_follow = RelationShip.objects.get_or_create(from_user=from_user, to_user=self.request.user)
        if is_follow:
            return Response({'follow', relation.to_user.username, relation.from_user.username},
                            status=status.HTTP_201_CREATED)
        else:
            relation.delete()
            return Response({'{} unfollow {}'.format()}, status=status.HTTP_200_OK)
