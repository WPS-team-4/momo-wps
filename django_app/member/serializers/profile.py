from rest_framework import serializers

from map.serializers import MapDetailSerializer
from member.models import MomoUser, RelationShip

__all__ = (
    'RelationShipSerializer',
    'UserSerializer',
    'UserProfileSerializer',
)


class RelationShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationShip
        fields = (
            'to_user',
            'from_user',
            'created_date',
        )


class UserSerializer(serializers.ModelSerializer):
    # map_list = MapSerializer(many=True, read_only=True, source='map_set')

    # follower = RelationShipSerializer(many=True, read_only=True, source='follower_set')

    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'profile_img',
        )


class UserProfileSerializer(serializers.ModelSerializer):
    map_list = MapDetailSerializer(read_only=True, many=True, source='map_set')

    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'email',
            'profile_img',
            'following',
            'date_joined',
            'is_facebook',
            'is_active',
            'is_staff',
            'map_list',
        )

        # def update(self, instance, validated_data):
        #     instance.profile_img = validated_data.get('profile_img', instance.profile_img)
        #     instance.save()
        #     return instance
        #     instance.email = validated_data.get('email', instance.email)
