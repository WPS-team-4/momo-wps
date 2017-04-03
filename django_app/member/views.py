import datetime

from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import JSONWebTokenSerializer, VerifyJSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView

from member.serializers import UserSerializer, LoginSerializer

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class ProfileViewAPI(JSONWebTokenAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = VerifyJSONWebTokenSerializer

    # def get_serializer(self, *args, **kwargs):
    #     serializer_class = self.get_serializer_class()
    #     kwargs['token'] = self.get_serializer_context()
    #     return serializer_class(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # user = request.user
        data = request.data('Authentication')
        serializer = VerifyJSONWebTokenSerializer(data)
        if serializer.is_valid():
            user = request.user

            # toke = serializer.object.get('token')
            # response_data = jwt_response_payload_handler(token, user, request)
            # response = Response(response_data)

            # verify_jwt_token
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(JSONWebTokenAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (authentication.JSONWebTokenAuthentication,)
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

        # def post(self, request, *args, **kwargs):
        #     serializer = self.get_serializer(data=request.data)
        #
        #     if serializer.is_valid():
        #         user = serializer.object.get('user') or request.user
        #         token = serializer.object.get('token')
        #         response_data = jwt_response_payload_handler(token, user, request)
        #         response = Response(response_data)
        #         if api_settings.JWT_AUTH_COOKIE:
        #             expiration = (datetime.utcnow() +
        #                           api_settings.JWT_EXPIRATION_DELTA)
        #             response.set_cookie(api_settings.JWT_AUTH_COOKIE,
        #                                 response.data['token'],
        #                                 expires=expiration,
        #                                 httponly=True)
        #         return response
        #
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
