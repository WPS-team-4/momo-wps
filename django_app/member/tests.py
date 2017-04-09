from django.test import TransactionTestCase

from utils.tests import make_dummy_users


class MomoUserModelTest(TransactionTestCase):
    def test_follow(self):
        users = make_dummy_users(10)
        users[0].follow(users[1])
        users[0].follow(users[2])
        users[0].follow(users[3])

        users[1].follow(users[3])
        users[1].follow(users[2])

        users[2].follow(users[3])

        self.assertIn(users[1], users[0].following.all())
        self.assertIn(users[2], users[0].following.all())
        self.assertIn(users[3], users[0].following.all())

        self.assertIn(users[2], users[1].following.all())
        self.assertIn(users[3], users[1].following.all())

        self.assertIn(users[3], users[2].following.all())

        self.assertIn(users[0], users[3].follower_set.all())
        self.assertIn(users[1], users[3].follower_set.all())
        self.assertIn(users[2], users[3].follower_set.all())

        self.assertIn(users[0], users[2].follower_set.all())
        self.assertIn(users[1], users[2].follower_set.all())

        self.assertIn(users[0], users[1].follower_set.all())
