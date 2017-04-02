import datetime

from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt import authentication
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class LoginAPI(JSONWebTokenAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (authentication.JSONWebTokenAuthentication,)
    serializer_class = JSONWebTokenSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = LoginSerializer(request.data)
    #     user = authenticate(username=serializer.data['email'], password=serializer.data['password'])
    #     if user is not None:
    #         token = Token.objects.get_or_create(user=user)[0]
    #         views.obtain_jwt_token
    #         return Response({"token": str(token)}, status=status.HTTP_200_OK)
    #     else:
    #         error = {
    #             "error": ""
    #         }
    #     return Response(error, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    response.data['token'],
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
