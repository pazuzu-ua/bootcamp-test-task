from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='COAX Bootcamp Homework',
        default_version='v1',
        description='This api was created as part of the COAX Bootcamp.',
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
)

swagger_pattern = path('', schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui")
