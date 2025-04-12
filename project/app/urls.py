from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path, include
from .views import (FoodAPIView, FoodDetailAPIView, CustomerAPIView, CustomerDetailAPIView,
                        BuyurtmaAPIView, BuyurtmaDetailAPIView)

urlpatterns = [
    path('food/', FoodAPIView.as_view()),
    path('food/<int:food_id>', FoodDetailAPIView.as_view()),

    path('customer/', CustomerAPIView.as_view()),
    path('customer/<int:customer_id>', CustomerDetailAPIView.as_view()),

    path('order/', BuyurtmaAPIView.as_view()),
    path('order/<int:order_id>', BuyurtmaDetailAPIView.as_view()),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Sizning API nomingiz",
        default_version='v1',
        description="API hujjatlari",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="you@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    re_path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('', include('your_app.urls')),
]