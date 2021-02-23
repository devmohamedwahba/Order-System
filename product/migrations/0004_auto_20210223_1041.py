# Generated by Django 3.1.7 on 2021-02-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_fill_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='exchange_rate',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='total_exchange',
        ),
        migrations.AlterField(
            model_name='currency',
            name='price',
            field=models.DecimalField(decimal_places=8, max_digits=14),
        ),
    ]