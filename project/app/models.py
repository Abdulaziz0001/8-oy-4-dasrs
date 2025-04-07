from django.db import models
from django.db.models import CharField


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    soni = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phonnumber = CharField(max_length=13)

    def __str__(self):
        return self.fullname

class Buyurtma(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    sana = models.DateTimeField()
