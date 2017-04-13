from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import MomoUser
from member.serializers import RelationShipSerializer

__all__ = (
    'FollowAPI',
)


class FollowAPI(APIView):
    serializer_class = RelationShipSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        from_user_pk = self.kwargs['pk']
        print(from_user_pk)
        # self.request.data['from_user'] = self.request.user
        # self.request.data['to_user'] = MomoUser.objects.get(id=from_user_pk)
        # from_user = MomoUser.objects.get(id=from_user_pk)
        # to_user = self.request.user
        # print(self.request.data.get('from_user'))
        # print(self.request.data.get('to_user'))
        # print(self.request.data)
        data = {
            'from_user': MomoUser.objects.get(id=from_user_pk),
            'to_user': self.request.user
        }
        serializer = RelationShipSerializer(data=data)
        # serial_data = serializer(to_user=self.request.user, from_user=MomoUser.objects.get(id=from_user_pk))
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
