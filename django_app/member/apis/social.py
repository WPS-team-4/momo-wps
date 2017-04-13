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
        serializer = RelationShipSerializer
        from_user_pk = self.kwargs['pk']
        print(from_user_pk)
        request.data['from_user'] = MomoUser.objects.get(id=from_user_pk)
        request.data['to_user'] = self.request.user
        serial_data = serializer(data=request.data)
        if serial_data.is_valid():
            serial_data.save()

        return Response(serial_data)
