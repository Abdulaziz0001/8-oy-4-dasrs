from django.urls import path
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
