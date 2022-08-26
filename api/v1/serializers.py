from rest_framework.serializers import ModelSerializer
from apps.orders.models import Product, Order


class ProductSerializer(ModelSerializer):
    """This is a Product serializer."""

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    """This is an Order serializer."""

    class Meta:
        model = Order
        fields = '__all__'
