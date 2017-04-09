from django.test import TransactionTestCase


class MomoUserModelTest(TransactionTestCase):
    def test_follow(self):
        users = make_dummy_users()