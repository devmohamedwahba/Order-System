from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from product.models import Product, Currency

from product.serializers import ProductSerializer

PRODUCT_URL = reverse('product:product-list')


def detail_url(product_id):
    return reverse('product:product-detail', args=[product_id])


def sample_currency():
    return Currency.objects.create(name='EGP', price=10)


def sample_user(email="Test@gmail.com", password="P@ssw0rd"):
    return get_user_model().objects.create_user(email, password)


class PublicProductApiTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(PRODUCT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateProductApiAdminTest(TestCase):
    def setUp(self) -> None:
        self.admin = get_user_model().objects.create_user(email='test@gmail.com', password='password', is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(self.admin)

    def test_retrieve_products(self):
        Product.objects.create(
            name="Test Product 1",
            owner=sample_user(),
            quantity=10,
            price="10.00000000",
            currency=sample_currency()
        )

        res = self.client.get(PRODUCT_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        payload = {
            'name': "Test Product 1",
            'quantity': 10,
            'price': "10.00000000",
            'currency': sample_currency().id,
        }
        res = self.client.post(PRODUCT_URL, payload)
        exists = Product.objects.filter(
            name=payload['name']
        ).exists()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)
