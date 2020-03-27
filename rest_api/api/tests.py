from django.test import TestCase
from .models import CategoryModel, PostModel
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .serializers import PostSerializer, CategorySerializer
import json
from users.models import CustomUser


class CategoryModelTestCase(TestCase):
    def setUp(self) -> None:
        self.category_name = 'Ads'
        self.category = CategoryModel(name=self.category_name)

    def test_model_can_create_category(self):
        old_count = CategoryModel.objects.count()
        self.category.save()
        new_count = CategoryModel.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(self.category), self.category_name)


class PostModelTestCase(TestCase):
    def setUp(self) -> None:
        self.category_name = 'Ads'
        self.user_instance = CustomUser.objects.create_user(username='sherlock', email='holmes@gmail.com', password='holmesqwert5678')
        self.category_instance = CategoryModel.objects.create(name=self.category_name)
        self.title = 'Some Titile'
        self.content = 'Some Content'
        self.post = PostModel.objects.create(author=self.user_instance, title=self.title, content=self.content)
        self.post.category.add(self.category_instance)

    def test_model_can_create_post(self):
        old_count = PostModel.objects.count()
        self.post = PostModel.objects.create(author=self.user_instance, title=self.title+"2", content=self.content)
        self.post.category.add(self.category_instance)
        self.post.save()
        new_count = PostModel.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test  for the api views."""

    def setUp(self) -> None:
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.category_data = {'name': 'Science'}

        self.user_instance = CustomUser.objects.create_user(username='sheldon', email='cooper@gmail.com', password='qwert5678')
        self.client.force_authenticate(self.user_instance)
        self.category_response = self.client.post(
            reverse('create_category'),
            self.category_data,
            format="json")
        self.category_instance = CategoryModel.objects.first()
        self.title = 'big bang theory'
        self.content = 'some bazinga'
        self.post = PostModel.objects.create(author=self.user_instance, title=self.title, content=self.content)
        self.post.category.add(self.category_instance)
        self.category_name = CategoryModel.objects.first().name

    def test_create_a_valid_post(self):
        self.post_data_valid = {

            "author": self.user_instance.id,
            "title": "friends",
            "content": "some url",
            "category": [
                self.category_name,
            ]
        }
        response = self.client.post(reverse('create_posts'),
                                    data=json.dumps(self.post_data_valid),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_an_invalid_post(self):
        self.post_data_invalid2 = {

            "author": self.user_instance.id,
            "title": "",
            "content": "https://github.com/gitgik/django-rest-api/blob/master/rest_api/tests.py",
            "category": [
                self.category_name,
            ]
        }
        response = self.client.post(reverse('create_posts'),
                                    data=json.dumps(self.post_data_invalid2),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_valid_single_post(self):
        response = self.client.get(reverse('post_details', kwargs={'pk':self.post.id}))
        test_post = PostModel.objects.get(pk=self.post.pk)
        serializer = PostSerializer(test_post)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_invalid_single_post(self):
        response  = self.client.get(reverse('post_details',kwargs={'pk':1000000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_post(self):
        self.post_valid_update = {

            "author": self.user_instance.id,
            "title": "coldplay",
            "content": "No Url",
            "category": [
                self.category_name,
            ]
        }
        response = self.client.put(reverse('post_details', kwargs={'pk':self.post.id}),
                                           data=json.dumps(self.post_valid_update),
                                           content_type= 'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post_currentUser(self):

        self.post_valid_update2 = {

            "author": "",
            "title": "maroon5",
            "content": "No Url",
            "category": [
                self.category_name,
            ]
        }
        response = self.client.put(reverse('post_details', kwargs={'pk': self.post.id}),
                                   data=json.dumps(self.post_valid_update2),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = self.client.delete(
            reverse('post_details', kwargs={'pk': self.post.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_post(self):
        response = self.client.delete(
            reverse('post_details', kwargs={'pk': "300"}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_create_a_category(self):
        self.assertEqual(self.category_response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_category(self):
        category = CategoryModel.objects.get()
        response = self.client.get(
            reverse('category_details',
                    kwargs={'pk': category.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, category)

    def test_api_can_update_a_category(self):
        change_category = {'name': 'Computer'}
        category = CategoryModel.objects.get()
        res = self.client.put(reverse('category_details', kwargs={'pk': 1}),
                              change_category, format='json'
                              )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_category(self):
        category = CategoryModel.objects.get()
        response = self.client.delete(
            reverse('category_details', kwargs={'pk': 1}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


