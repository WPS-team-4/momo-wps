from rest_framework import serializers

# from map.serializers import MapSerializer
from member.models import MomoUser

__all__ = (
    'UserSerializer',
    # 'UserProfileSeializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'profile_img',
        )


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
