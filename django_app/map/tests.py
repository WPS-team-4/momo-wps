import random

from django.contrib.auth import get_user_model
from django.urls import NoReverseMatch
from django.urls import resolve
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APILiveServerTestCase

from map.models import Map
from utils.tests.testcase_api import APITestCaseAuthMixin

User = get_user_model()


class MapModelTest(APITestCaseAuthMixin, APILiveServerTestCase):
    def test_apis_url_exist(self):
        try:
            # 1. MapList에 대한 url view가 존재하는지 확인
            resolve('/api/map/')
            # 2. MapDetail에 대한 url view가 존재하는지 확인
            resolve('/api/map/1/')
        except NoReverseMatch as e:
            self.fail(e)

    def test_map_create(self):
        user = self.create_user_and_login(self.client)

        response = self.create_map(1)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # response의 key값 검사
        self.assertIn('author', response.data)
        self.assertIn('map_name', response.data)
        self.assertIn('description', response.data)
        self.assertIn('created_date', response.data)
        self.assertIn('is_private', response.data)
        # print('response_data: {}'.format(response.data))

        # response의 author 값 검사
        response_auth = response.data['author']
        self.assertIn('username', response_auth)

        self.assertEqual(Map.objects.count(), 1)
        new_map = Map.objects.first()
        self.assertEqual(new_map.author.id, user.id)
        # print(response_auth)

    def test_cannot_map_create__not_authenticated(self):
        # 인증되지 않은 사용자가 map을 create 할 수 있는지 확인
        url = reverse('api:post-list')
        response = self.client.post(url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Map.objects.exists(), False)

    def test_map_list(self):

        # map list 확인
        self.create_user_and_login(self.client)
        num = random.randrange(1, 10)
        self.create_map(num)
        url = reverse('api:map-list')
        response = self.client.get(url)
        print(response)

    def test_map_update_partial(self):
        pass

    def test_map_retrieve(self):
        pass

    def test_map_destroy(self):
        pass
