from django.test import TestCase
from django.contrib.auth import get_user_model
from product.models import Product, Currency


def sample_user(email="Test@gmail.com", password="P@ssw0rd"):
    return get_user_model().objects.create_user(email, password)


def sample_currency():
    return Currency.objects.create(name='EGP', price=10)


class ProductModelTest(TestCase):
    def test_product_str(self):
        product = Product.objects.create(
            name="Test Product",
            owner=sample_user(),
            quantity=10,
            price=20,
            currency=sample_currency()

        )
        self.assertEqual(str(product), product.name)
