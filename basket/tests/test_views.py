from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self) -> None:
        """To create date for testing"""
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django-beginners', slug='django-beginners', price='20.00', image='django', created_by_id=1)
        Product.objects.create(category_id=1, title='django-beginners', slug='django-beginners', price='20.00', image='django', created_by_id=1)
        Product.objects.create(category_id=1, title='django-beginners', slug='django-beginners', price='20.00', image='django', created_by_id=1)
        Product.objects.create(category_id=1, title='django-beginners', slug='django-beginners', price='20.00', image='django', created_by_id=1)
        self.client.post(
            reverse('basket:basket_add'), {'productid': 1, 'productqty': 1, 'action': 'post'}, xhr=True
        )
        self.client.post(
            reverse('basket:basket_add'), {'productid': 2, 'productqty': 2, 'action': 'post'}, xhr=True
        )
        # return super().setUp()

    def test_basket_url(self):
        """Test Homepage response status"""
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """Test adding items to basket"""
        response = self.client.post(
            reverse('basket:basket_add'), {'productid': 3, 'productqty': 1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('basket:basket_add'), {'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        """Test delete items from basket"""
        response = self.client.post(
            reverse('basket:basket_delete'), {'productid': 2, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '20.00'})

    def test_basket_update(self):
        """Test update items in basket"""
        response = self.client.post(
            reverse('basket:basket_update'), {'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.00'})
