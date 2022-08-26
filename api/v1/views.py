from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from apps.orders.models import Order, Product
from api.v1.serializers import OrderSerializer, ProductSerializer


class OrderView(ListCreateAPIView):
    """This is a view for Orders."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(ModelViewSet):
    """This represents a view for a Product."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
