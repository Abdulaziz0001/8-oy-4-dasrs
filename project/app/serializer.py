from rest_framework import serializers
from .models import Food, Customer, Buyurtma

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'price', 'soni']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['fullname', 'email', 'phonnumber']


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = ['customer', 'food', 'sana']