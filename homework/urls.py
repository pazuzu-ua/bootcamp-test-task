from django.contrib import admin
from django.urls import path, include
from api.v1.routes import router
from api.v1.views import OrderView
from .yasg import swagger_pattern

urlpatterns = [
    swagger_pattern,
    path(r'admin/', admin.site.urls),
    path(r'api/v1/', include(router.urls)),
    path(r'api/v1/orders/', OrderView.as_view(), name='orders'),
]
