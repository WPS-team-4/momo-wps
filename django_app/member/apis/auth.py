# from pprint import pprint

import requests
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from member.models import MomoUser
from member.serializers import LoginSerializer, UserSerializer

__all__ = (
    'SignUpAPI',
    'LoginAPI',
    'LogoutAPI',
    'FacebookLoginAPI',
)


class SignUpAPI(CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(self.request.data)
        serializer.is_valid()
        user = authenticate(serializer.validated_data)
        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            response = Response({"user": {
                "pk": user.pk,
                "token": token.key}
            }, status=status.HTTP_200_OK)
            return response
        else:
            error = {
                "error": ""
            }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        user = request.user
        if user:
            request.auth.delete()
            return Response({'정상적으로 로그아웃 되었습니다'}, status=status.HTTP_200_OK)
        error = {
            "error": "",
        }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class FacebookLoginAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        APP_ID = settings.config['facebook']['app_id']
        SECRET_CODE = settings.config['facebook']['secret_code']
        APP_ACCESS_TOKEN = '{app_id}|{secret_code}'.format(
            app_id=APP_ID,
            secret_code=SECRET_CODE
        )
        ASCII_USER_ACCESS_TOKEN = request.data.get('access_token')
        USER_ACCESS_TOKEN = ASCII_USER_ACCESS_TOKEN.encode('utf-8')

        url_debug_token = 'https://graph.facebook.com/debug_token'
        params = {
            'scopes': 'public_profile, email',
            'input_token': USER_ACCESS_TOKEN,
            'access_token': APP_ACCESS_TOKEN,
        }

        r = requests.get(url_debug_token, params=params)
        dict_debug_token = r.json()

        if dict_debug_token['data']['is_valid']:
            facebook_id = dict_debug_token['data']['user_id']
            fb_user_info = self.get_fb_user_info(facebook_id, USER_ACCESS_TOKEN)
            user, _ = MomoUser.objects.get_or_create(
                password=facebook_id,
                username=facebook_id,
            )
            user.is_facebook = True

            token, _ = Token.objects.get_or_create(user=user)
            response = Response({"token": token.key}, status=status.HTTP_200_OK)
            return response
        else:
            return Response({'error': dict_debug_token['data']['error']['message']}, status=status.HTTP_400_BAD_REQUEST)

    def get_fb_user_info(self, facebook_id, access_token):
        USER_ID = facebook_id
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

        return dict_user_info
