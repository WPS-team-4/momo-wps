from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from pin.models import Pin
from post.models import Post
from post.serializers.post import PostSerializer

__all__ = (
    'PostList',
    'PostDetail',
)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        data = request.data
        # print('request_data: {}'.format(data))
        pin = Pin.objects.get(id=data.get('pin'))
        photo = data.get('photo')
        file = request.FILES['photo']
        description = data.get('description')

        print('pin: {}, photo: {}, decription: {}'.format(pin, photo, description))
        if photo or description:

            if description and photo:
                # print('*******')
                post = Post.objects.create(
                    pin=pin,
                    photo=file,
                    description=description
                )
            elif description is False:
                # print('@@@@@@@@')
                post = Post.objects.create(
                    pin=pin,
                    photo=file,
                )
            else:
                # print('!!!!!!!!')
                post = Post.objects.create(
                    pin=pin,
                    description=description
                )

            serializer = PostSerializer(post)
            print('serializer.data: {}'.format(serializer.data))

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            raise ValidationError(detail="photo와 description 중 한가지 값은 꼭 입력해주세요.")

    def perform_create(self, serializer):
        serializer.save()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
