from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView

from shop.models import Product, Category
from .serializer import ProductSerializer, CategorySerializer

@api_view(['GET'])
def categories(request):
    if request.method == 'GET':
        categories=Category.objects.all()
        serializer=CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        products=Product.objects.all()
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer