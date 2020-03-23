from django.test import TestCase
from .models import CategoryModel


# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self) -> None:
        self.category_name = 'Ads'
        self.category = CategoryModel(name = self.category_name)

    def test_model_can_create_category(self):
        old_count = CategoryModel.objects.count()
        self.category.save()
        new_count = CategoryModel.objects.count()
        self.assertNotEqual(old_count, new_count)

