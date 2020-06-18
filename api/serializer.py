from rest_framework import serializers

from shop.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'slug', 'name', 'parent')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'slug', 'image', 'description', 'price', 'avialable', 'created', 'updated', 'views')