from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MomoUserManager(BaseUserManager):
    """
    암호화 부분 구현할 것
    """

    def create_user(self, username, profile_img=None, password=None):
        user = MomoUser(username=username, password=password)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        user = MomoUser(username=username, password=password)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save()

        return user


class MomoUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)

    email = models.EmailField(blank=True)
    password = models.CharField(max_length=100)
    profile_img = models.ImageField(blank=True, upload_to='member')
    facebook_id = models.CharField(max_length=100, blank=True)
    is_facebook = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MomoUserManager()

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
