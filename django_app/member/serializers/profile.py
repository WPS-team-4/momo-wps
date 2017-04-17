from rest_framework import serializers
from rest_framework.compat import set_many
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from map.serializers import MapDetailSerializer
from member.models import MomoUser, RelationShip
from utils import DynamicFieldsModelSerializer

__all__ = (
    'UserSerializer',
    'UserProfileSerializer',
    'RelationShipSerializer',
)


class RelationShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationShip
        fields = (
            'to_user',
            'from_user',
            'created_date',
        )


class UserSerializer(DynamicFieldsModelSerializer):
    # following = RelationShipSerializer(source='relation_user_set.relation_to_user')
    # followers = RelationShipSerializer(source='relation_user_set.relation_from_user')
    map_list = MapDetailSerializer(read_only=True, many=True, source='map_set')

    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'password',
            'email',
            'profile_img',
            'relation_user_set',
            # 'following',
            # 'followers',
            'date_joined',
            'last_login',
            'is_facebook',
            'is_active',
            'is_staff',
            'is_superuser',
            'map_list',
        )
        extra_kwargs = {'password': {'write_only': True}}

        read_only_fields = (
            'pk',
            'following',
            'followers',
            'map_list',
        )

    def create(self, validated_data):
        user = MomoUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                set_many(instance, attr, value)
            else:
                setattr(instance, attr, value)

        password = validated_data.get('password')
        if password:
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
