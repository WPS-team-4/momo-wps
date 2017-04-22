import requests
from django.contrib.auth import authenticate
from django.core.exceptions import MultipleObjectsReturned
from django.http import Http404
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from config import settings
from member.models import MomoUser
from member.serializers import LoginSerializer
from member.serializers import UserCreateSerializer
from member.serializers import UserSerializer
from member.views import send_auth_mail

__all__ = (
    'SignUpAPI',
    'LoginAPI',
    'LogoutAPI',
    'FacebookLoginAPI',
    'UserActivateAPI',
    'UserAuthMailAPI',
)


class SignUpAPI(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        request.data['userid'] = username
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            headers = self.get_success_headers(serializer.data)
            send_auth_mail(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.pop('username')[0]
        request.data["userid"] = username
        serializer = LoginSerializer(request.data)
        user = authenticate(userid=serializer.data['userid'], password=serializer.data['password'])
        if user:
            is_active = user.is_active
            if is_active:
                token, _ = Token.objects.get_or_create(user=user)
                response = Response({"token": token.key,
                                     "user_pk": token.user_id,
                                     "created": token.created}, status=status.HTTP_200_OK)
                return response
            else:
                detail = "인증 메일을 확인해주세요."
                raise PermissionDenied(detail=detail)
        else:
            detail = "사용자를 찾을 수 없습니다. username과 password를 다시 확인해주세요."
        raise ValidationError(detail=detail)


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
        USER_ACCESS_TOKEN = request.data.get("access_token")
        url_debug_token = 'https://graph.facebook.com/debug_token'
        params = {
            'input_token': USER_ACCESS_TOKEN,
            'access_token': APP_ACCESS_TOKEN,
        }

        r = requests.get(url_debug_token, params=params)
        dict_debug_token = r.json()

        if dict_debug_token['data']['is_valid']:
            facebook_id = dict_debug_token['data']['user_id']
            fb_user_info = self.get_fb_user_info(facebook_id, USER_ACCESS_TOKEN)
            fb_user_photo = self.get_fb_user_photo(facebook_id, USER_ACCESS_TOKEN)
            # fb_user_info로 default username을 생성
            fb_username = '{} {}'.format(fb_user_info['last_name'], fb_user_info['first_name'])
            fb_email = fb_user_info['email']

            # fb_user_info에서 profile img 가져오기
            fb_profile_img = fb_user_photo['data']['url']

            user, is_created = MomoUser.objects.get_or_create(userid=facebook_id)
            if is_created:
                user.username = fb_username
                user.set_password(facebook_id)
                user.profile_img = fb_profile_img
                user.is_facebook = True
                user.email = fb_email

            else:
                if user.profile_img is None:
                    user.profile_img = fb_profile_img
                if user.email is None:
                    user.email = fb_email

            user.save()

            token, _ = Token.objects.get_or_create(user=user)

            serializer = UserSerializer(user)
            result = serializer.data
            result["is_created"] = is_created
            response = Response(result, status=status.HTTP_200_OK)
            return response
        else:
            return Response({'error': dict_debug_token['data']['error']['message']}, status=status.HTTP_400_BAD_REQUEST)

    def get_fb_user_info(self, facebook_id, access_token):
        USER_ID = facebook_id
        url_api_user = 'https://graph.facebook.com/v2.9/{user_id}?fields='.format(
            user_id=USER_ID
        )
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
        ]
        params = {
            'fields': ','.join(fields),
            'access_token': access_token
        }
        r = requests.get(url_api_user, params)
        dict_user_info = r.json()

        return dict_user_info

    def get_fb_user_photo(self, facebook_id, access_token):
        USER_ID = facebook_id
        url_api_user_photo = 'https://graph.facebook.com/v2.9/{user_id}/picture?type=large&redirect=0'.format(
            user_id=USER_ID)
        r = requests.get(url_api_user_photo)
        dict_user_photo = r.json()
        return dict_user_photo


class UserActivateAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        try:
            key = request.query_params['key']
            user = MomoUser.objects.get(hash_username=key)
            user.is_active = True
            user.save()
        except MomoUser.DoesNotExist:
            raise Http404
        except MultipleObjectsReturned:
            raise ValidationError(detail="인증 요청 url이 잘못 되었습니다.")
        except MultiValueDictKeyError:
            raise ValidationError(detail="인증 요청 url이 잘못 되었습니다.")

        return Response({"user_pk": user.pk,
                         "detail": "user가 활성화되었습니다.",
                         "url": reverse('index', request=request)}, status=status.HTTP_200_OK,
                        template_name='member/activate.html')


class UserAuthMailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            pk = request.data['pk']
            user = MomoUser.objects.get(pk=pk)
            send_auth_mail(user=user)
            return Response({"detail": "인증메일이 발송되었습니다"}, status=status.HTTP_200_OK)
        except MomoUser.DoesNotExist:
            raise Http404(detail="user가 존재하지 않습니다.")
        except ValueError:
            raise ValidationError(detail="user pk가 올바른 형식이 아닙니다.")
