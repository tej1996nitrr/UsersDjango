from django.test import TestCase
from .models import CategoryModel, ContentModel
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .serializers import  CategorySerializer,ContentSerializer
import json
from accounts.models import Profile


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

class ContentModelTestCase(TestCase):

    def setUp(self) -> None:
        self.category_name = 'Ads'
        self.user_instance = User.objects.create_user(username='macbook', email='nerd@gmail.com', password='qwert5678')
        self.profile_instance = Profile.objects.get(user=self.user_instance)
        self.category_instance = CategoryModel.objects.create(name=self.category_name)
        self.title = 'pycharm'
        self.content = 'Bazinga.@haha.com'
        self.content =ContentModel.objects.create(author=self.profile_instance,title=self.title,content=self.content)
        self.content.category.add(self.category_instance)

    def test_model_can_create_content(self):
        old_count = ContentModel.objects.count()
        self.category_name = 'Ads2'
        self.user_instance = User.objects.create_user(username='macbook2', email='nerd2@gmail.com', password='qwert5678')
        self.profile_instance = Profile.objects.get(user=self.user_instance)
        self.category_instance = CategoryModel.objects.create(name=self.category_name)
        self.title = 'pycharm2'
        self.content = 'Bazinga2.@haha.com'
        self.content = ContentModel.objects.create(author=self.profile_instance, title=self.title, content=self.content)
        self.content.category.add(self.category_instance)
        new_count = ContentModel.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self) -> None:
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.category_data = {'name': 'Science'}
        self.category_response = self.client.post(reverse('create_category'), self.category_data, format="json")
        self.user_instance = User.objects.create_user(username='nerd', email='nerd@gmail.com', password='qwert5678')
        self.category_instance = CategoryModel.objects.first()
        self.title = 'Batman'
        self.content = 'some url'
        self.profile_instance = Profile.objects.get(user=self.user_instance)
        self.content = ContentModel.objects.create(author=self.profile_instance, title=self.title, content=self.content)
        self.content.category.add(self.category_instance)
        self.client.force_authenticate(self.profile_instance)
        # print(self.profile_instance.id)
        # print(self.user_instance.id)


    def test_get_valid_single_post(self):
        response = self.client.get(reverse('content_details', kwargs={'pk':self.content.id}))
        test_post = ContentModel.objects.get(pk=self.content.pk)
        serializer = ContentSerializer(test_post)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_invalid_single_post(self):
        response  = self.client.get(reverse('content_details',kwargs={'pk':300}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_post(self):
        self.post_valid_update = {

            "author": self.profile_instance.id,
            "title": "pycharm",
            "content": "No Url",
            "category": [
                1,
            ]
        }
        response = self.client.put(reverse('content_details', kwargs={'pk':self.content.id}),
                                           data=json.dumps(self.post_valid_update),
                                           content_type= 'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = self.client.delete(
            reverse('content_details', kwargs={'pk': self.content.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_post(self):
        response = self.client.delete(
            reverse('content_details', kwargs={'pk': 300}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_create_a_category(self):
        """Test the api has category creation capability."""
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
        res = self.client.put(reverse('category_details', kwargs={'pk': category.id}),
                              change_category, format='json'
                              )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_category(self):
        """Test the api can delete a category"""
        category = CategoryModel.objects.get()
        response = self.client.delete(
            reverse('category_details', kwargs={'pk': category.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
