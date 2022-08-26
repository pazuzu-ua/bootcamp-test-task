from rest_framework.serializers import ModelSerializer, ValidationError
from apps.orders.models import Product, Order


class ProductSerializer(ModelSerializer):
    """This is a Product serializer."""

    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_price(self, value):
        """This ensures the price is good."""
        kopeks = float(value % 1)
        if kopeks % .25 != .0:
            raise ValidationError('The kopeks amount should be multiple of .25')
        return value


class OrderSerializer(ModelSerializer):
    """This is an Order serializer."""

    class Meta:
        model = Order
        fields = '__all__'
