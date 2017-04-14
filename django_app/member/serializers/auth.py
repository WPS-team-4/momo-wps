from rest_framework import serializers

from member.models import MomoUser

__all__ = (
    'LoginSerializer',
)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomoUser
        fields = (
            'username',
            'password',
        )