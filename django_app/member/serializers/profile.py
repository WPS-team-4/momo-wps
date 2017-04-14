from rest_framework import serializers
from rest_framework.compat import set_many
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from map.serializers import MapDetailSerializer
from member.models import MomoUser

__all__ = (
    'UserSerializer',
    'UserProfileSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomoUser
        fields = (
            'id',
            'username',
            'password',
            'email',
            'profile_img',
            'date_joined',
            'last_login',
            'is_facebook',
            'is_active',
            'is_staff',
            'is_superuser',
        )
        extra_kwargs = {'password': {'write_only': True}}

        read_only_fields = (
            'id',
        )

    def create(self, validated_data):
        user = MomoUser.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                set_many(instance, attr, value)
            else:
                setattr(instance, attr, value)

        # instance.profile_img = validated_data.get('profile_img', instance.profile_img)
        # instance.email = validated_data.get('email', instance.email)

        if password:
            password = validated_data.get('password')
            instance.set_password(password)

        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    map_list = MapDetailSerializer(read_only=True, many=True, source='map_set')

    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'email',
            'profile_img',
            'relation',
            'follower',
            'following',
            'date_joined',
            'is_facebook',
            'is_active',
            'is_staff',
            'map_list',
        )
