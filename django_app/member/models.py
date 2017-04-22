from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.dispatch import receiver
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


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
    userid = models.CharField(max_length=100)
    description = models.CharField(max_length=140, blank=True, null=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=100)
    profile_img = VersatileImageField(
        'Headshot',
        upload_to='headshot/',
        blank=True,
    )
    is_facebook = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    relation = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='relation_user_set',
        through='RelationShip',
    )

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    hash_username = models.CharField(blank=True, max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MomoUserManager()

    def __str__(self):
        return str(self.pk)

    def get_short_name(self):
        return self.username

    def follow(self, user):
        self.relation_from_user.create(
            to_user=user,
        )

    def unfollow(self, user):
        self.relation_from_user.filter(
            to_user=user
        ).delete()

    @property
    def following(self):
        relations = self.relation_from_user.all()
        return MomoUser.objects.filter(id__in=relations.values('to_user_id'))

    @property
    def followers(self):
        relations = self.relation_to_user.all()
        return MomoUser.objects.filter(id__in=relations.values('from_user_id'))


@receiver(models.signals.post_save, sender=MomoUser)
def warm_User_headshot_images(sender, instance, **kwargs):
    user_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='headshot',
        image_attr='profile_img',
        verbose=True
    )
    num_created, failed_to_create = user_img_warmer.warm()


class RelationShip(models.Model):
    from_user = models.ForeignKey(MomoUser, related_name='relation_from_user')
    to_user = models.ForeignKey(MomoUser, related_name='relation_to_user')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('from_user', 'to_user')
        )

    def __str__(self):
        return 'Relation from({},{}) to({},{})'.format(
            self.from_user.username, self.from_user.pk, self.to_user.username, self.to_user.pk)
