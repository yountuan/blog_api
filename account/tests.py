from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.contrib.auth import get_user_model
from .views import RegistrationView, LoginView, LogoutView, ChangePasswordView


class AuthTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create_user(
            email='testuser@gmail.com',
            password='123456789',
            is_active=True,
            activation_code='1234'
        )

    def test_registration(self):
        data = {
            'email': 'new_test_user_@gmail.com',
            'password': '12345',
            'password_confirm': '12345',
            'name': 'Test'
        }
        request = self.factory.post('api/v1/account/register/', data, format='json')
        print(request)
        print('============')
        view = RegistrationView.as_view()
        response = view(request)
        # print(response)
        # print('------')
        # assert response.status_code == 201
        assert get_user_model().objects.filter(email=data['email']).exists

    def test_login(self):
        data = {
            'email': 'testuser@gmail.com',
            'password': '123456789'
        }
        request = self.factory.post('login/', data, format='json')
        view = LoginView.as_view()
        response = view(request)
        # assert response.status_code == 201
        assert 'token' in response.data

    def test_change_password(self, ):
        data = {
            'password': '123456789',
            'new_password': '54321'
        }
        request = self.factory.post('change-password/', data, format='json')
        force_authenticate(request, user=self.user)
        # print(request)
        view = ChangePasswordView.as_view()
        response = view(request)
        print(response, response.data)
        assert response.status_code == 200

    def test_forgot_password(self):
        data = {
            'email': 'testuser@gmail.com'
        }
        request = self.factory.post('forgot-password/', data)
