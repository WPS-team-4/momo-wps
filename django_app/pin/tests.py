import random

from django.test import TestCase

from member.models import MomoUser
from utils import make_dummy_hash_tags
from utils import make_dummy_users
from utils.tests.testcase import TEST_NAME, TEST_PLACE_NAME
from .models import Map, Pin, Place, PinHashTag


class PinModelTest(TestCase):
    def test_users_create_each_pins_with_same_place(self):
        users = make_dummy_users(5)
        place = Place.objects.create(
            name='test bucks',
            address='Seoul',
            lat='123',
            lng='456',
            place_id='125'
        )
        maps = []
        for i in range(5):
            map = Map.objects.create(
                author=users[i],
                map_name='test_map{}'.format(i + 1),
                description='I_am_test_map{}, Hello world!'.format(i + 1)
            )
            maps.append(map)

        pins = []
        for i in range(5):
            pin = Pin.objects.create(
                place=place,
                map=maps[i],
                pin_name='test 0331'
            )
            pins.append(pin)

        self.assertEqual(Pin.objects.filter(place=place).count(), 5)
        print(Pin.objects.filter(place=place))


class HashTagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = MomoUser.objects.create(
            username='test_user{}{}'.format(1, 1),
            password='test_password'
        )

        cls.place = Place.objects.create(
            name='{}{}'.format(random.choice(TEST_NAME), random.choice(TEST_PLACE_NAME)),
            address='{}나라 {}번지'.format(random.choice(TEST_NAME), 111),
            lat='lat: {}'.format(random.randrange(100, 120)),
            lng='lng: {}'.format(random.randrange(100, 120)),
        )

        cls.map = Map.objects.create(
            author=cls.user,
            name='{} 지도'.format(random.choice(TEST_NAME)),
            description='{}번째 지도입니다.'.format(1),
        )

    def test_add_different_hash_tags_with_same_pin(self):
        tags = make_dummy_hash_tags(10)
        # places = make_dummy_places(1)
        # maps = make_dummy_maps(1)
        # users = make_dummy_users(1)

        pin = Pin.objects.create(
            author=self.user,
            place=self.place,
            map=self.map,
            name='{}{}'.format(random.choice(TEST_NAME), random.choice(TEST_PLACE_NAME)),
        )

        for tag in tags:
            PinHashTag.objects.create(
                hash_tag=tag,
                pin=pin
            )
        self.assertEqual(pin.pinhashtag_set.filter(pin=pin).count(), 10)
        print(pin.pinhashtag_set.filter(pin__author=self.user))
