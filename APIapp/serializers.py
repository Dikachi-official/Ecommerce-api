from dataclasses import field
from rest_framework import serializers      #TO SERIALIZE A DATA TO A JSON FORMAT
from .models import *
from django.contrib.auth.models import User


class CategorySerializer (serializers.ModelSerializer):

    class Meta:
        fields = ('id','title')    #FROM THE CATEGORY MODEL
        model = Category



class BookSerializer (serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username') # TO DISPLAY USERNAME INSTEAD OF ID IN FRONTEND
    class Meta:                  #FROM THE BOOK MODEL
        fields = (
            'id',
            'title',
            'author',
            'category',
            'isbn', 
            'price', 
            'quantity',
            'price',
            'description',
            'img_url',
            'status',
            'creator',
            'created_on'
        )     
        model = Book 



class ProductSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')  # TO DISPLAY USERNAME INSTEAD OF ID IN FRONTEND
    class Meta:
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'description',
            'quantity',
            'created_on',
            'creator',
            'img_url',
            'status'
        )

        model = Product



# FOR USER
class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all()),
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        fields = (         #FOR THE USER MODEL
            'id',
            'username',
            'email',
            'books',
            'products'
        )

        model = User
