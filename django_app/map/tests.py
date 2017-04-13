<<<<<<< HEAD
from django.test import TestCase

# Create your tests here.
=======
import random

from django.test import TestCase

from map.models import Map
from utils.tests.testcase import TEST_NAME, make_dummy_users


class MapModelTest(TestCase):
    def test_create_new_map(self):
        user = make_dummy_users(1)[0]
        name = random.choice(TEST_NAME)
        Map.objects.create(
            author=user,
            name=name,
            description='lasdjlfjskldjfl',
        )
        map = Map.objects.get(author=user)
        self.assertEqual(map.name, name)
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
