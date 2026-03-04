from .models import Product, Products_Category, Maker
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

class ProductsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Products_Category
        fields = '__all__'
        depth = 1

class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = '__all__'
        depth = 1