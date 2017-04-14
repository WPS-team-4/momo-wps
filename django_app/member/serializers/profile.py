from rest_framework import serializers

from map.serializers import MapDetailSerializer
from member.models import MomoUser

__all__ = (
    # 'RelationShipSerializer',
    'UserSerializer',
    'UserProfileSerializer',
)


class UserSerializer(serializers.ModelSerializer):
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

# class RelationShipSerializer(serializers.ModelSerializer):
#     to_user = UserSerializer(read_only=True)
#     from_user = UserSerializer(read_only=True)
#
#     class Meta:
#         model = RelationShip
#         fields = (
#             'to_user',
#             'from_user',
#             'created_date',
#         )
