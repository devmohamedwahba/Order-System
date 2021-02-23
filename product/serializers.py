from rest_framework import serializers
from .models import Product, Currency, Order, OrderProduct


class CustomProductSerializer(serializers.Serializer):
    """
    custom serializer to send product and amount
    """
    id = serializers.IntegerField()
    quantity = serializers.IntegerField(write_only=True)


class ProductSerializer(serializers.ModelSerializer):
    """
    serializer for product object
    """

    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'price', 'currency', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class CurrencySerializer(serializers.ModelSerializer):
    """
    currency serializer
    """

    class Meta:
        model = Currency
        fields = ('id', 'name', 'price', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):
    """
    order serializer
    """
    products = CustomProductSerializer(many=True)

    def create(self, validated_data):
        products = validated_data.pop('products')
        order = self.Meta.model.objects.create(**validated_data)
        order_total = 0
        for product in products:
            product_item = Product.objects.get(id=product.get('id'))
            if product_item and product_item.quantity > 0:
                product_price_in_euro = product_item.price / product_item.currency.price
                all_product_total_exchange_in_euro = product_price_in_euro * product.get('quantity')

                OrderProduct.objects.create(product_id=product_item, order_id=order, quantity=product.get('quantity'),
                                            price=product_price_in_euro, exchange_rate=product_item.currency.price,
                                            total_exchange=all_product_total_exchange_in_euro,
                                            currency_product_id=product_item.currency.id)
                product_item.quantity -= product.get('quantity')
                product_item.save()
                order_total += all_product_total_exchange_in_euro
        order.total = order_total
        order.exchange_rate = order.order_currency.price
        order.total_exchange = order.exchange_rate * order.total
        order.save()
        return order

    class Meta:
        model = Order
        fields = ('id', 'user', 'products', 'total', 'order_currency', 'total_exchange','created_at', 'updated_at')
        read_only_fields = ('id', 'user', 'total', 'total_exchange','created_at', 'updated_at')
