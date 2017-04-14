from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import MomoUser

__all__ = (
    'FollowAPI',
)


class FollowAPI(APIView):
    # serializer_class = RelationShipSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        to_user = MomoUser.objects.get(id=self.kwargs['pk'])
        from_user = self.request.user
        # relation, is_follow = RelationShip.objects.get_or_create(from_user=from_user, to_user=to_user)
        # print(relation)
        is_following = to_user in list(from_user.following)

        if is_following:
            from_user.unfollow(to_user)
            return Response({"from_user": from_user.pk,
                             "to_user": to_user.pk,
                             "status": "unfollow"},
                            status=status.HTTP_200_OK)
        else:
            from_user.follow(to_user)
            return Response({"from_user": from_user.pk,
                             "to_user": to_user.pk,
                             "status": "follow"},
                            status=status.HTTP_201_CREATED)
