from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from .models import Food, Customer, Buyurtma
from .serializer import FoodSerializer, BuyurtmaSerializer, CustomerSerializer
from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle

# Custom throttle klass
class CustomRateThrottle(UserRateThrottle):
    rate = '3/minute'



class FoodAPIView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    throttle_classes = [CustomRateThrottle]



class FoodDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_url_kwarg = "food_id"
    throttle_classes = [CustomRateThrottle]



class CustomerAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    throttle_classes = [CustomRateThrottle]



class CustomerDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_url_kwarg = "customer_id"
    throttle_classes = [CustomRateThrottle]



class BuyurtmaAPIView(ListCreateAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    throttle_classes = [CustomRateThrottle]



class BuyurtmaDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    lookup_url_kwarg = "order_id"
    throttle_classes = [CustomRateThrottle]