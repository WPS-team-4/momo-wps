from rest_framework import serializers
from rest_framework.compat import set_many
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
from versatileimagefield.serializers import VersatileImageFieldSerializer

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
    following = serializers.SerializerMethodField(read_only=True)
    followers = serializers.SerializerMethodField(read_only=True)
    map_list = MapDetailSerializer(read_only=True, many=True, source='map_set')
    profile_img = VersatileImageFieldSerializer(sizes='headshot')

    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'password',
            'auth_token',
            'email',
            'profile_img',
            'description',
            'following',
            'followers',
            'date_joined',
            'last_login',
            'is_facebook',
            'is_active',
            'is_staff',
            'is_superuser',
            'map_list',
        )
        extra_kwargs = {'password': {'write_only': False}}

        read_only_fields = (
            'pk',
            'following',
            'followers',
            'map_list',
            'auth_token',
            'profile_img',
            'description',
        )

    @staticmethod
    def get_followers(obj):
        followers = RelationShip.objects.filter(to_user_id=obj.id)
        follower_list = list(followers)
        ret = []
        for follower in follower_list:
            ret.append(follower.from_user_id)
        return ret

    @staticmethod
    def get_following(obj):
        followings = RelationShip.objects.filter(from_user_id=obj.id)
        following_list = list(followings)
        ret = []
        for following in following_list:
            ret.append(following.to_user_id)
        return ret

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
    profile_img = VersatileImageFieldSerializer(sizes='headshot')

    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'email',
            'profile_img',
            'description',
            'relation',
            'follower',
            'following',
            'date_joined',
            'is_facebook',
            'is_active',
            'is_staff',
            'map_list',
        )
