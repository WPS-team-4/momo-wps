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
        from_user_pk = self.kwargs['pk']
        # print(from_user_pk)
        self.request.data['from_user'] = self.request.user.pk
        self.request.data['to_user'] = from_user_pk
        # from_user = MomoUser.objects.get(id=from_user_pk)
        # to_user = self.request.user
        # print(self.request.data.get('from_user'))
        # print(self.request.data.get('to_user'))
        # print(self.request.data)
        # data = {}
        # data['from_user'] = MomoUser.objects.get(id=from_user_pk),
        # data['to_user'] = self.request.user
        # serializer = RelationShipSerializer(data=data)
        # serial_data = serializer(to_user=self.request.user, from_user=MomoUser.objects.get(id=from_user_pk))
        # if serializer.is_valid():
        #     serializer.save()

        # return Response(serializer.data)
        from_user = MomoUser.objects.get(id=from_user_pk)
        relation, is_follow = RelationShip.objects.get_or_create(from_user=from_user, to_user=self.request.user)
        # serializer = RelationShipSerializer(data=relation)
        # serializer.is_valid()
        if is_follow:
            return Response({'follow', relation.to_user.username, relation.from_user.username}, status=status.HTTP_201_CREATED)
        else:
            relation.delete()
            return Response({'unfollow'}, status=status.HTTP_200_OK)
