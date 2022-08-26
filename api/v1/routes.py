from rest_framework import routers
from api.v1.views import ProductViewSet
from django.urls import path


router = routers.DefaultRouter()

router.register(
    r'products', 
    ProductViewSet, 
    basename='products'
)
