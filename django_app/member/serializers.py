from django.contrib.auth import get_user_model
from rest_framework import serializers

from member.models import MomoUser

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'password',
            'profile_img',
            'email',
            'date_joined',
            'facebook_id',
            'is_facebook',
            'is_superuser',
            'is_staff',
            'is_active',
        )

        # def update(self, instance, validated_data):
        #     instance.profile_img = validated_data.get('profile_img', instance.profile_img)
        #     instance.email = validated_data.get('email', instance.email)
        #     instance.save()
        #     return instance


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
