import random

from django.test import TestCase

from member.models import MomoUser
from .models import Map, Pin, Place, HashTag, PinHashTag

TEST_NAME = '피카츄', '라이츄', '파이리', '꼬부기', '버터플', '야도란', '피존투', '또가스'
TEST_PLACE_NAME = '맛집', '주유소', '카페', '호텔', '도서관', 'PC방', '은행', '우체국'


def make_dummy_users(num):
    users = []

    for i in range(num):
        user = MomoUser.objects.create_user(
            username='test_user{}'.format(i + 1),
            password='test_password'
        )
        users.append(user)
    return users


def make_dummy_places(num):
    places = []
    for i in range(num):
        place = Place.objects.create(
            name='{}{}'.format(random.choice(TEST_NAME), random.choice(TEST_PLACE_NAME)),
            address='{}나라 {}번지'.format(random.choice(TEST_NAME), i),
            lat='lat: {}'.format(random.randrange(100, 120)),
            lng='lng: {}'.format(random.randrange(100, 120)),
            place_id='g_place_id: {}'.format(random.randrange(111, 999))
        )
        places.append(place)
    return places


def make_dummy_hash_tags(num):
    tags = []
    for i in range(num):
        tag = HashTag.objects.create(
            content='#{}번째_태그'.format(i + 1)
        )
        tags.append(tag)
    return tags


def make_dummy_maps(num):
    maps = []
    users = make_dummy_users(1)
    for i in range(num):
        map = Map.objects.create(
            author=users[0],
            name='{} 지도'.format(random.choice(TEST_NAME)),
            description='{}번째 지도입니다.'.format(i + 1),
        )
        maps.append(map)
    return maps


def make_pins(num_place, num_map, num_user, num_pin):
    pins = []
    places = make_dummy_places(num_place)
    maps = make_dummy_maps(num_map)
    users = make_dummy_users(num_user)
    for i in range(num_pin):
        pin = Pin.objects.create(
            author=users[i],
            place=places[i],
            map=maps[i],
            name='{}{}'.format(random.choice(TEST_NAME), random.choice(TEST_PLACE_NAME)),
        )
        pins.append(pin)
    return pins


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
