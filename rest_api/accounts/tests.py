from django.test import TestCase
import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):
    """Creating test cases for Reg"""
    def test_registration(self):
        data = {"username": "sherlock", "email": "holmes@localhost.app",
                "password1": "BakersStreet", "password2": "BakersStreet"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_for_invalid_password(self):
        data = {"username": "sherlock", "email": "holmes@localhost.app",
                "password1": "Baker", "password2": "Baker"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_for_invalid_email(self):
        data = {"username": "sherlock", "email": "holmes",
                "password1": "BakersStreet", "password2": "BakersStreet"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_for_passwords_unmatch(self):
        data = {"username": "sherlock", "email": "holmes@localhost.app",
                "password1": "BakersStreet", "password2": "BakersStreet2"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_null_password(self):
        data = {"username": "sherlock", "email": "holmes@localhost.app",
                "password1": "", "password2": ""}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_null_username(self):
        data = {"username": "", "email": "holmes@localhost.app",
                "password1": "BakersStreet", "password2": "BakersStreet"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_existing_username(self):
        self.user = User.objects.create_user(username="holmes",
                                             password="some-very-strong-psw")
        data = {"username": "holmes", "email": "holmes@localhost.app",
                "password1": "BakersStreet", "password2": "BakersStreet"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_token(self):
        data = {"username": "holmes", "email": "holmes@localhost.app",
                "password1": "BakersStreet", "password2": "BakersStreet"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertTrue('key' in response.data)


class ProfileTestCase(APITestCase):
    """Creating test cases for profiles"""
    list_url = reverse("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(username="holmes",
                                             password="some-very-strong-psw")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse("profile-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "holmes")

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
                                   {"city": "Hyd", "bio": "Renaissance Genius"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {"id": 1, "user": "holmes", "bio": "Renaissance Genius",
                          "city": "Hyd", "profile_pic": None,"content":[]})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(username="random",
                                               password="psw123123123")
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
                                   {"bio": "hacked!!!"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



