from django.db import models
from utils.models import TimestampedModel
from django.conf import settings


class Currency(TimestampedModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=8, max_digits=14)

    def __str__(self):
        return str(self.name)


class Product(TimestampedModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=8, max_digits=14)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrderProduct(TimestampedModel):
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    currency_product = models.ForeignKey(Currency, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=8, max_digits=14)
    quantity = models.IntegerField()
    exchange_rate = models.DecimalField(decimal_places=2, max_digits=8)
    total_exchange = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        db_table = 'order_product'


class Order(TimestampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    order_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=8, max_digits=14, null=True)
    exchange_rate = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    total_exchange = models.DecimalField(decimal_places=8, max_digits=14, null=True)

    def __str__(self):
        return str(self.user)
