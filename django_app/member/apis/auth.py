import datetime
from pprint import pprint

import requests
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_decode_handler, jwt_payload_handler, \
    jwt_encode_handler
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView

from config import settings
from member.models import MomoUser
from member.serializers import LoginSerializer, CreateUserSerializer

__all__ = (
    'SignUpAPI',
    'LoginAPI',
    'LogoutAPI',
    'FacebookLoginAPI',
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


class FacebookLoginAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        APP_ID = settings.config['facebook']['app_id']
        SECRET_CODE = settings.config['facebook']['secret_code']
        # REDIRECT_URI = 'http://localhost:8000/member/login/facebook/'
        APP_ACCESS_TOKEN = '{app_id}|{secret_code}'.format(
            app_id=APP_ID,
            secret_code=SECRET_CODE
        )

        USER_ACCESS_TOKEN = request.data.get('access_token')
        print('ACCESS TOKEN : %s' % USER_ACCESS_TOKEN)

        url_debug_token = 'https://graph.facebook.com/debug_token'
        params = {
            'scopes': 'public_profile, email',
            'input_token': USER_ACCESS_TOKEN,
            'access_token': APP_ACCESS_TOKEN,
        }

        r = requests.get(url_debug_token, params=params)
        dict_debug_token = r.json()
        pprint(dict_debug_token)

        # facebook_id = dict_debug_token['data']['user_id']
        # fb_user_info = self.get_fb_user_info(facebook_id, USER_ACCESS_TOKEN)

        # return Response(fb_user_info)
        if dict_debug_token['data']['is_valid']:
            facebook_id = dict_debug_token['data']['user_id']
            fb_user_info = self.get_fb_user_info(facebook_id, USER_ACCESS_TOKEN)
            user, _ = MomoUser.objects.get_or_create(
                facebook_id=facebook_id,
                password=facebook_id,
                username=facebook_id,
            )
            user.is_facebook = True
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = Response({"token": token}, status=status.HTTP_200_OK)
            return response
        else:
            return Response({'error': dict_debug_token['data']['error']['message']}, status=status.HTTP_400_BAD_REQUEST)

    def get_fb_user_info(self, facebook_id, access_token):
        USER_ID = facebook_id
        print('USER ID: %s' % USER_ID)

        # 해당 USER_ID 로 graph API에 유저정보를 요청
        url_api_user = 'https://graph.facebook.com/{user_id}'.format(
            user_id=USER_ID
        )
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'picture',
            'email',
        ]
        params = {
            'fields': ','.join(fields),
            'access_token': access_token
        }
        r = requests.get(url_api_user, params)
        dict_user_info = r.json()
        pprint(dict_user_info)

        return dict_user_info
