import random

from django.test import TestCase
from django.urls import NoReverseMatch
from django.urls import resolve
from django.urls import reverse
from rest_framework import status

from map.models import Map
from utils.tests.testcase import TEST_NAME, make_dummy_users


class MapModelTest(TestCase):
    def test_apis_url_exist(self):
        try:
            # 1. MapList에 대한 url view가 존재하는지 확인
            resolve('/api/map/')
            # 2. MapDetail에 대한 url view가 존재하는지 확인
            resolve('/api/map/1/')
        except NoReverseMatch as e:
            self.fail(e)

    def create_map(self, num=1):
        # Map을 생성하는 API주소를 reverse
        url = reverse('api:map-list')
        for i in range(num):
            response = self.client.post(url)
            if num == 1:
                return response

    def test_map_create(self):

        response = self.create_map()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = make_dummy_users(1)[0]
        map_name = random.choice(TEST_NAME)

        Map.objects.create(
            author=user,
            map_name=map_name,
            description='map description test',
        )
        map = Map.objects.get(author=user)
        self.assertEqual(map.map_name, map_name)

        # response의 key값 검사
        # response의 author 값 검사

    def test_cannot_map_create__not_authenticated(self):
        # 인증되지 않은 사용자가 map을 create 할 수 있는지 확인
        pass

    def test_map_list(self):
        # map list 확인
        pass

    def test_map_update_partial(self):
        pass

    def test_map_retrieve(self):
        pass

    def test_map_destroy(self):
        pass
