from django.test import TestCase


def make_dummy_users():
    users = []

    for i in range(10):
        user = MomoUser.objects.create_user(
            username='username{}'.format(i + 1),
            password='test_password'
        )
        users.append(user)
    return users


class MapTest(TestCase):
    pass
