from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from .models import Food, Customer, Buyurtma
from .serializer import FoodSerializer, BuyurtmaSerializer, CustomerSerializer


# Create your views here.

class FoodAPIView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self):
        if 5 > 0:
            pass
        return Food.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return FoodSerializer
        return FoodSerializer


class FoodDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_url_kwarg = "food_id"



class CustomerAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        if 5 > 0:
            pass
        return Food.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return FoodSerializer
        return FoodSerializer

class CustomerDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_url_kwarg = "customer_id"



class BuyurtmaAPIView(ListCreateAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer

    def get_queryset(self):
        if 5 > 0:
            pass
        return Food.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return FoodSerializer
        return FoodSerializer

class BuyurtmaDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    lookup_url_kwarg = "order_id"