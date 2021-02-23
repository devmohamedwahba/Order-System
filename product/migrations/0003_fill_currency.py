# Generated by Django 3.1.7 on 2021-02-23 09:17

from django.db import migrations
from utils.fixer import FixerApi
from django.conf import settings
from product.models import Currency


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0002_remove_order_total'),
    ]

    def get_currency(apps, schema_editor):
        fixer_api = FixerApi(base_url=settings.BASE_URL)
        currencies = fixer_api.get_all_exchange_rate_base_euro().get('rates')
        for name, price in currencies.items():
            Currency.objects.create(name=name, price=price)

    operations = [
        migrations.RunPython(get_currency),
    ]