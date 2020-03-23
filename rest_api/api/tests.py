from django.test import TestCase
from .models import CategoryModel,PostModel
from django.contrib.auth.models import User


# Create your tests here.
class CategoryModelTestCase(TestCase):
    def setUp(self) -> None:
        self.category_name = 'Ads'
        self.category = CategoryModel(name = self.category_name)

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
        self.post = PostModel.objects.create(author=self.user_instance , title=self.title, content=self.content)
        self.post.category.add(self.category_instance)

    def test_model_can_create_post(self):
        old_count = PostModel.objects.count()
        self.post = PostModel.objects.create(author=self.user_instance , title=self.title, content=self.content)
        self.post.category.add(self.category_instance)
        self.post.save()
        new_count = PostModel.objects.count()
        self.assertNotEqual(old_count, new_count)




