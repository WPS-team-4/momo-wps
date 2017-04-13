from rest_framework import serializers
from rest_framework.serializers import Serializer

from member.models import MomoUser

__all__ = (
    'LoginSerializer',
    'CreateUserSerializer',
    'TokenSerializer',
)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomoUser
        fields = (
            'username',
            'password',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomoUser
        fields = ('email', 'username', 'password')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MomoUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TokenSerializer(Serializer):
    access_token = serializers.CharField(read_only=True)
