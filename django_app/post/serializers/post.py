from rest_framework import serializers

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'author',
            'comment',
            'photo',
        )
        read_only_fields = (
            'created_date',
        )
