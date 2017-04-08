from rest_framework import serializers

from member.models import MomoUser
from post.models import Post
from post.serializers.post_comment import PostCommentSerializer
from post.serializers.post_photo import PostPhotoSerializer

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset=MomoUser.objects.all(), source='username')
    # author = UserSerializer(read_only=True)
    comment = PostCommentSerializer(read_only=True, many=True, source='postcomment_set')
    photo_list = PostPhotoSerializer(read_only=True, many=True, source='postphoto_set')

    class Meta:
        model = Post
        fields = (
            'pk',
            'pin',
            'author',
            'created_date',
            'comment',
            'photo_list',
        )
