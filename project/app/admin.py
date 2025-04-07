from django.contrib import admin
from .models import Food, Customer, Buyurtma

# Register your models here.

admin.site.register(Food)
admin.site.register(Customer)
admin.site.register(Buyurtma)