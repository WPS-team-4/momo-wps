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

# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MomoUser
#         fields = ('pk', 'email', 'username', 'password')
#         # extra_kwargs = {'password': {'write_only': True}}
#
#         read_only_fields = (
#             'pk',
#         )
#
#     def create(self, validated_data):
#         user = MomoUser.objects.create(
#             email=validated_data['email'],
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
