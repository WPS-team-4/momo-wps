import datetime

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_decode_handler
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView

from member.serializers import LoginSerializer, CreateUserSerializer

__all__ = (
    'SignUpAPI',
    'LoginAPI',
    'LogoutAPI',
)

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class SignUpAPI(CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = CreateUserSerializer

    def perform_create(self, serializer):
        serializer.save(data=self.request.data)


class LoginAPI(JSONWebTokenAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = JSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(request.data)
        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        if user is not None:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            # token = Token.objects.get_or_create(user=user)[0]
            # views.obtain_jwt_token
            response = Response({"token": token}, status=status.HTTP_200_OK)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    response.data['token'],
                                    expires=expiration,
                                    httponly=True)
            return response
        else:
            error = {
                "error": ""
            }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(JSONWebTokenAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = JSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        if user:
            request.auth = jwt_decode_handler(request.auth)

            request.auth.clear()
            return Response(request.auth, status=status.HTTP_200_OK)
            error = {
                "error": "",
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
