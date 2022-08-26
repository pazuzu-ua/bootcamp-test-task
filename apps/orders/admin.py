from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Order, Product


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """This is to register Order at admin site."""

    list_display = ('id', 'created_at', 'get_product_name', 'get_product_price')
    list_per_page = 25
    search_fields = ('get_product_name',)
    ordering = ('-created_at',)
    list_filter = ('created_at', 'product__name')

    def get_product_name(self, obj):
        return obj.product.name
    
    def get_product_price(self, obj):
        return obj.product.price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """This is to register Product at admin site."""

    list_display = ('id', 'name', 'price', 'description')
    list_per_page = 25
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    list_filter = ('created_at', 'name', 'price')
