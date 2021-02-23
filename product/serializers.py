from rest_framework import serializers
from .models import Product, Currency, Order, OrderProduct
from django.conf import settings


class CustomProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255),
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(decimal_places=2, max_digits=8)
    currency = serializers.IntegerField(write_only=True)
    amount = serializers.IntegerField(write_only=True)


class ProductSerializer(serializers.ModelSerializer):
    """
    serializer for product object
    """

    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'price', 'currency', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'price')
        read_only_fields = ('id', 'created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):
    products = CustomProductSerializer(many=True)

    def create(self, validated_data):
        products = validated_data.pop('products')
        order = self.Meta.model.objects.create(**validated_data)

        for product in products:
            OrderProduct.objects.create(product_id_id=product.get('id'), order_id=order, quantity=product.get('amount'),
                                        price=product.get('price'),
                                        currency_product_id=product.get('currency'))

        return order

    class Meta:
        model = Order
        fields = ('id', 'user', 'products', 'order_currency')
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')
