from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class APITestCaseAuthMixin(object):
    test_username = 'test_username'
    test_password = 'test_password'

    def create_user(self):
        user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        return user

    def create_user_and_login(self, client):
        user = self.create_user()
        client.login(username=self.test_username, password=self.test_password)
        return user

    def create_map(self, num=1):
        # Map을 생성하는 API주소를 reverse
        url = reverse('api:map-list')
        user = self.create_user_and_login(self.client)
        data = {
            'map_name': '카페지도',
            'author': user.username,
            'description': '다시 가고 싶은 카페 모으기'
        }
        for i in range(num):
            response = self.client.post(url, data, format='json')
            if num == 1:
                return response