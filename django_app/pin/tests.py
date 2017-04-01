import random

from django.test import TestCase

from member.models import MomoUser
from .models import Map, Pin, Place, HashTag

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


def make_dummy_plces(num):
    places = []
    for i in range(num):
        place = Place.objects.create(
            name='{}{}'.format(random.choice(TEST_NAME), random.choice(TEST_PLACE_NAME)),
            address='{}나라 {}번지'.format(random.choice(TEST_NAME), i),
            location='{}.{}'.format(random.randrange(111, 999), random.randrange(111, 999)),
        )
        places.append(place)
    return place


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
    places = make_dummy_plces(num_place)
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


class PinModelTest(TestCase):
    def test_users_create_each_pins_with_same_place(self):
        users = make_dummy_users(5)
        place = Place.objects.create(
            name='test bucks',
            address='Seoul',
            location='123.123',
            google_place_id='111'
        )
        maps = []
        for i in range(5):
            map = Map.objects.create(
                author=users[i],
                name='test_map{}'.format(i + 1),
                description='I_am_test_map{}, Hello world!'.format(i + 1)
            )
            maps.append(map)

        pins = []
        for i in range(5):
            pin = Pin.objects.create(
                author=users[i],
                place=place,
                map=maps[i],
                name='test 0331'
            )
            pins.append(pin)

        self.assertEqual(Pin.objects.filter(place=place).count(), 5)
