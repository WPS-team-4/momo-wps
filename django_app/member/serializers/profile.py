from rest_framework import serializers

<<<<<<< HEAD
# from map.serializers import MapSerializer
from member.models import MomoUser

__all__ = (
    'UserSerializer',
    # 'UserProfileSeializer',
)


class UserSerializer(serializers.ModelSerializer):
=======
from map.serializers import MapDetailSerializer
from member.models import MomoUser, RelationShip

__all__ = (
    'RelationShipSerializer',
    'UserSerializer',
    'UserProfileSerializer',
)


class RelationShipSerializer(serializers.ModelSerializer):
    to_user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    from_user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

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

>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'profile_img',
        )


<<<<<<< HEAD
# class UserProfileSeializer(serializers.ModelSerializer):
#     map_list = MapSerializer(read_only=True, many=True, source='map_set')
#
#     class Meta:
#         model = MomoUser
#         fields = (
#             'pk',
#             'username',
#             'profile_img',
#             'map_list',
#         )
=======
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
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
