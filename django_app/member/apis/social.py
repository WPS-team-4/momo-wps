from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import RelationShip, MomoUser

__all__ = (
    'FollowAPI',
)


class FollowAPI(APIView):
    # serializer_class = RelationShipSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        to_user = MomoUser.objects.get(id=self.kwargs['pk'])
        from_user = self.request.user
        relation, is_follow = RelationShip.objects.get_or_create(from_user=from_user, to_user=to_user)
        print(relation)
        if is_follow:
            return Response({"from_user": from_user.pk,
                             "to_user": to_user.pk,
                             "status": 'from_user{} follow to_user{}'.format(from_user.pk, to_user.pk)},
                            status=status.HTTP_201_CREATED)
        else:
            relation.delete()
            return Response({"from_user": from_user.pk,
                             "to_user": to_user.pk,
                             "status": 'from_user{} unfollow to_user{}'.format(from_user.pk, to_user.pk)},
                            status=status.HTTP_200_OK)
