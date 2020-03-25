from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json

class AccountsTest(APITestCase):

    def setUp(self):
        self.test_user = User.objects.create_user('testuser', 'test@gmail.com', 'testpassword')
        self.create_url = reverse('account-create')

    def test_create_user(self):
        data = {
            'username': 'sherlock',
            'email': 'holmes@holmes.com',
            'password': 'sherlocked',
            'confirm_password':'sherlocked'
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)
        self.assertTrue("token" in json.loads(response.content))

    def test_create_user_with_short_password(self):
        data = {
            'username': 'sherlock',
            'email': 'holmes@holmes.com',
            'password': 'som',
            'confirm_password': 'som'
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_no_password(self):
        data = {
            'username': 'sherlock',
            'email': 'sherlock@holmes.com',
            'password': '',
            'confirm_password': ''
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_long_username(self):
        data = {
            'username': 'holmes'*30,
            'email': 'holmes@example.com',
            'password': 'sherlocked',
            'confirm_password': 'sherlocked'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_with_no_username(self):
        data = {
            'username': '',
            'email': 'holmes@moriarty.com',
            'password': 'sherlocked',
            'confirm_password': 'sherlocked'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_existing_username(self):
        data = {
            'username': 'testuser',
            'email': 'user@example.com',
            'password': 'testuser',
            'confirm_password': 'testuser'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_existing_email(self):
        data = {
            'username': 'testuser2',
            'email': 'test@gmail.com',
            'password': 'testuser',
            'confirm_password': 'testuser'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_invalid_email(self):
        data = {
            'username': 'holmes',
            'email': 'testing',
            'passsword': 'watson',
            'confirm_password': 'watson'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_none_email(self):
        data = {
            'username': 'watson',
            'email': '',
            'password': 'watson',
            'confirm_password': 'watson'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_different_passwords(self):
        data = {
            'username': 'watson',
            'email': '',
            'password': 'holmes@123',
            'confirm_password': 'watson@123'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_users_view(self):
        response = self.client.get(reverse('account-allusers'),format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_current_users_view(self):
        response = self.client.post(reverse('account-login'), {"username": "testuser", "password": "testpassword"})
        content = json.loads(response.content)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + content['token'])
        response = self.client.get(reverse('account-me'),format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_user_view(self):
        response = self.client.get(reverse('account-details',kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentication_without_password(self):
        response = self.client.post(reverse('account-login'), {"username": "testuser"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_wrong_password(self):
        response = self.client.post(reverse('account-login'), {"username": "testuser", "password": "wrong"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_valid_data(self):
        response = self.client.post(reverse('account-login'), {"username": "testuser", "password": "testpassword"})
        self.assertEqual(200, response.status_code)
        self.assertTrue("token" in json.loads(response.content))









