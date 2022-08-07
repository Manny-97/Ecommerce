from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self) -> None:
        """ Set up test data inside the db """
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """Test Category model data insertion/types/field attributes"""
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):

    def setUp(self) -> None:
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='Muhammed')
        self.data1 = Product.objects.create(category_id=1, title='django-beginners', slug='django-beginners', price='20.00', image='django', created_by_id=1)
        # return super().setUp()

    def test_product_model_entry(self):
        """ """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django-beginners')
