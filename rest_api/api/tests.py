from django.test import TestCase
from .models import CategoryModel, PostModel
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .serializers import PostSerializer, CategorySerializer
import json

class CategoryModelTestCase(TestCase):
    """Tests for Category Model."""
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
    """Tests for Post Model."""
    def setUp(self) -> None:
        self.category_name = 'Ads'
        self.user_instance = User.objects.create_user(username='nerd', email='nerd@gmail.com', password='qwert5678')
        self.category_instance = CategoryModel.objects.create(name=self.category_name)
        self.title = 'pycharm'
        self.content = 'some url'
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
    """Tests api views."""

    def setUp(self) -> None:
        """Defining the test client and other test variables."""
        self.client = APIClient()
        self.category_data = {'name': 'Science'}
        self.category_response = self.client.post(
            reverse('create_category'),
            self.category_data,
            format="json")
        self.user_instance = User.objects.create_user(username='nerd', email='nerd@gmail.com', password='qwert5678')
        self.client.force_authenticate(self.user_instance)
        self.category_instance = CategoryModel.objects.first()
        self.title = 'pycharm'
        self.content = 'some url'
        self.post = PostModel.objects.create(author=self.user_instance, title=self.title, content=self.content)
        self.post.category.add(self.category_instance)
        self.post_data = {

            "author": self.user_instance.id,
            "title": "Flask",
            "content": "https://github.com/gitgik/django-rest-api/blob/master/rest_api/tests.py",
            "category": [
                1,
            ]
        }
        self.post_response = self.client.post(
            reverse('create_posts'),
            self.post_data,
            format="json")

        self.post_data_valid = {

            "author": self.user_instance.id,
            "title": "vscode",
            "content": "some url",
            "category": [
                1,
            ]
        }
        self.post_data_invalid = {

            "author": self.user_instance.id,
            "title": "pycharm",
            "content": "some url",
            "category": [
                1,
            ]
        }
        self.post_valid_update = {

            "author": self.user_instance.id,
            "title": "pycharm",
            "content": "No Url",
            "category": [
                1,
            ]
        }
        self.post_invalid_update = {

            "author": "",
            "title": "pycharm",
            "content": "No Url",
            "category": [
                1,
            ]
        }
        self.post_data_invalid2 = {

            "author": self.user_instance.id,
            "title": "",
            "content": "https://github.com/gitgik/django-rest-api/blob/master/rest_api/tests.py",
            "category": [
                1,
            ]
        }

    def test_create_a_valid_post(self):
        """Test for creating a valid post"""
        response = self.client.post(reverse('create_posts'),
                                    data=json.dumps(self.post_data_valid),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_an_invalid_post(self):
        """Test for invalid post details"""
        response = self.client.post(reverse('create_posts'),
                                    data=json.dumps(self.post_data_invalid2),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_valid_single_post(self):
        """Test for valid single post details"""
        response = self.client.get(reverse('post_details', kwargs={'pk':self.post.id}))
        test_post = PostModel.objects.get(pk=self.post.pk)
        serializer = PostSerializer(test_post)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_invalid_single_post(self):
        """Test for invalid single post details"""
        response  = self.client.get(reverse('post_details',kwargs={'pk':300}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_post(self):
        """Test for valid update details"""
        response = self.client.put(reverse('post_details', kwargs={'pk':self.post.id}),
                                           data=json.dumps(self.post_valid_update),
                                           content_type= 'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_post(self):
        """Test for invalid update details"""
        response = self.client.put(reverse('post_details', kwargs={'pk': self.post.id}),
                                   data=json.dumps(self.post_invalid_update),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_post(self):
        """Test for valid delete details"""
        response = self.client.delete(
            reverse('post_details', kwargs={'pk': self.post.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_post(self):
        """Test for invalid delete details"""
        response = self.client.delete(
            reverse('post_details', kwargs={'pk': 300}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_create_a_category(self):
        """Test the api has category creation capability."""
        self.assertEqual(self.category_response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_category(self):
        """Test the api can get a category w id"""
        category = CategoryModel.objects.get()
        response = self.client.get(
            reverse('category_details',
                    kwargs={'pk': category.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, category)

    def test_api_can_update_a_category(self):
        """Test the api can update a category"""
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

    def test_api_can_create_a_post(self):
        """Test the api has category creation capability."""
        self.assertEqual(self.post_response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_post(self):
        """Test if the api can get a Post w id."""
        post = PostModel.objects.first()
        response = self.client.get(
            reverse('post_details',
                    kwargs={'pk': post.id}), format="json",follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, post)

    def test_api_can_update_a_post(self):
        """Test if the api can update a Post."""
        change_post = {

            "author": 1,
            "title": "Flask2",
            "content": "https://github.com/gitgik/django-rest-api/blob/master/rest_api/tests.py",
            "category": [
                1,

            ]
        }
        post = PostModel.objects.first()
        res = self.client.put(reverse('post_details', kwargs={'pk': post.id}),
                              change_post, format='json'
                              )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_post(self):
        """Test the api can delete a Post."""
        post = PostModel.objects.all()[:1].get()
        response = self.client.delete(
            reverse('post_details', kwargs={'pk': post.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)




