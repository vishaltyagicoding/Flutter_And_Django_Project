from django.contrib import admin
from .models import Products_Category, Maker, Product
# Register your models here.
admin.site.register(Products_Category)
admin.site.register(Maker)
admin.site.register(Product)