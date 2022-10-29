from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, BookSerializer, ProductSerializer, UserSerializer, RegistrationSerializer, CartSerializer
from . models import Category, Book, Product, Cart
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import serializers
import uuid






class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)

        # METHOD 1
        # serializer.is_valid(raise_exception = True)
        # serializer.save()

        #METHOD 2
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                "User" : serializer.data}, status=status.HTTP_201_CREATED
            )
        return Response({"Errors": serializers.errors}, status = status.HTTP_400_BAD_REQUEST)    





class ListCategory(generics.ListCreateAPIView):     #INHERITS ATRRIBUTES FROM GENERICS
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()               #FROM OUR MODELS
    serializer_class = CategorySerializer           #FROM SERIALIZERS.PY

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ListBook(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class ListProduct(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer    


#CART VIEW
class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset  = Cart.objects.all()  
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer      