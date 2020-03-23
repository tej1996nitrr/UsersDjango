from django.test import TestCase
from .models import CategoryModel, PostModel
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


# Create your tests here.
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
        self.user_instance = User.objects.create_user(username='nerd', email='nerd@gmail.com', password='qwert5678')
        self.category_instance = CategoryModel.objects.create(name=self.category_name)
        self.title = 'pycharm'
        self.content = 'some url'
        self.post = PostModel.objects.create(author=self.user_instance, title=self.title, content=self.content)
        self.post.category.add(self.category_instance)

    def test_model_can_create_post(self):
        old_count = PostModel.objects.count()
        self.post = PostModel.objects.create(author=self.user_instance, title=self.title, content=self.content)
        self.post.category.add(self.category_instance)
        self.post.save()
        new_count = PostModel.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self) -> None:
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.category_data = {'name': 'Science'}
        self.category_response = self.client.post(
            reverse('create_category'),
            self.category_data,
            format="json")
        self.post_data = {

            "author": 1,
            "title": "Flask",
            "content": "https://github.com/gitgik/django-rest-api/blob/master/rest_api/tests.py",
            "category": [
                1,
                2
            ]
        }
        self.post_response = self.client.post(
            reverse('create_posts'),
            self.category_data,
            format="json")

    def test_api_can_create_a_category(self):
        """Test the api has bucket creation capability."""
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

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        category = CategoryModel.objects.get()
        response = self.client.delete(
            reverse('category_details', kwargs={'pk': category.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_create_a_post(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.category_response.status_code, status.HTTP_201_CREATED)
