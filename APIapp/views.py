from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, BookSerializer, ProductSerializer, UserSerializer
from . models import Category, Book, Product
from django.contrib.auth.models import User

# Create your views here.

class ListCategory(generics.ListCreateAPIView):     #INHERITS ATRRIBUTES FROM GENERICS
    queryset = Category.objects.all()               #FROM OUR MODELS
    serializer_class = CategorySerializer           #FROM SERIALIZERS.PY

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    