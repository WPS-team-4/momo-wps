from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotAcceptable
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from member.models import MomoUser
from utils import IsOwnerOrReadOnly

__all__ = (
    'FollowAPI',
)


class FollowAPI(UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def patch(self, request, *args, **kwargs):
        print(self.kwargs)
        to_user = MomoUser.objects.get(id=self.kwargs['pk'])
        print(to_user)
        from_user = self.request.user
        if to_user == from_user:
            raise NotAcceptable(detail="자기 자신은 follow할 수 없습니다")
        else:
            is_following = to_user in list(from_user.following)

            if is_following:
                from_user.unfollow(to_user)
                response = Response({"from_user": from_user.pk,
                                     "to_user": to_user.pk,
                                     "status": "unfollow"},
                                    status=status.HTTP_204_NO_CONTENT)

            else:
                from_user.follow(to_user)
                response = Response({"from_user": from_user.pk,
                                     "to_user": to_user.pk,
                                     "status": "follow"},
                                    status=status.HTTP_201_CREATED)

        return response
