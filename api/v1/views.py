from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from apps.orders.models import Order, Product
from apps.orders.tasks import big_brother
from api.v1.serializers import OrderSerializer, ProductSerializer
from api.v1.permissions import OnlyAdminsCanDelete
from django_filters.rest_framework import DjangoFilterBackend


class OrderView(ListCreateAPIView):
    """This is a view for Orders."""

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('product__name',)
    serializer_class = OrderSerializer
    ordering_fields = ('created_at')
    permission_classes = (OnlyAdminsCanDelete,)

    def get_queryset(self):
        queryset = Order.objects.all()
        product = self.request.query_params.get('product')
        if product is not None:
            queryset = queryset.filter(product__name__contains=product)
        return queryset


class ProductViewSet(ModelViewSet):
    """This represents a view for a Product."""

    queryset = Product.objects.all()
    permission_classes = (OnlyAdminsCanDelete,)
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('name', 'description')
    search_fields = ('name', 'description')
    ordering_fields = ('created_at', 'name', 'price')

    def retrieve(self, request, *args, **kwargs):
        key = kwargs.get('pk')
        big_brother(key)
        return super().retrieve(request, *args, **kwargs)
