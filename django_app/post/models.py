from django.db import models

from config import settings
from member.models import MomoUser
from pin.models import Pin


class Post(models.Model):
    pin = models.ForeignKey(Pin)
    author = models.ForeignKey(MomoUser)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(
            self.pk
        )

        # def add_comment(self, user, content):
        #     return self.postcomment_set.create(
        #         author=user,
        #         contnet=content
        #     )
        #
        # def add_photo(self, user, photo):
        #     return self.postphoto_set.create(
        #         author=user,
        #         photo=photo
        #     )


class PostPhoto(models.Model):
    post = models.ForeignKey(Post)
    photo = models.ImageField(upload_to='post')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        order_with_respect_to = 'post'

    def to_dict(self):
        ret = {
            'pk': self.pk,
            'photo': self.photo.url,
        }
        return ret


class PostComment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    contents = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(
            self.contents
        )
