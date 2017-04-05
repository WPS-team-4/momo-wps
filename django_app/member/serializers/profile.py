from rest_framework import serializers

from map.serializers import MapSerializer
from member.models import MomoUser

__all__ = (
    'UserSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    map_list = MapSerializer(many=True, read_only=True, source='map_set')

    class Meta:
        model = MomoUser
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
            'map_list',
        )

        # def update(self, instance, validated_data):
        #     instance.profile_img = validated_data.get('profile_img', instance.profile_img)
        #     instance.email = validated_data.get('email', instance.email)
        #     instance.save()
        #     return instance
