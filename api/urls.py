from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Top Tier Binary API",
        default_version='v1',
        description="API documentation for the TTB project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="caleb@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)

swagger_documentation_endpoint = path(
    'documentation/', schema_view.with_ui(  # new
        'swagger', cache_timeout=0), name='schema-swagger'),

router = routers.DefaultRouter()

user = router.register('users', views.UserViewSet)
transaction = router.register('transactions', views.TransactionViewSet, basename='transactions')

urlpatterns = router.urls + list(swagger_documentation_endpoint)
