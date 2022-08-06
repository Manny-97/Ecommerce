from unicodedata import name
from django.test import TestCase
from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self) -> None:
        """
            Set up test data inside the db
        """
        self.data1 = Category.objects.create(name='django', slug='django')
        # return super().setUp()


    def test_category_model_entry(self):
        """
            Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_category_model_entry(self):
        """ """
        data = self.data1
        self.assertEqual(str(data), 'django')