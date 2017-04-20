from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from member.models import MomoUser

__all__ = (
    'DynamicFieldsModelSerializer',
    'AuthorSerializer',
)


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class AuthorSerializer(serializers.ModelSerializer):
    profile_img = VersatileImageFieldSerializer(sizes='headshot')

    class Meta:
        model = MomoUser
        fields = (
            'pk',
            'username',
            'profile_img',
        )
