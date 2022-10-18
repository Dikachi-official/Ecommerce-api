from dataclasses import field
from rest_framework import serializers      #TO SERIALIZE A DATA TO A JSON FORMAT
from .models import *


class CategorySerializer (serializers.ModelSerializer):

    class Meta:
        fields = ('id','title')    #FROM THE CATEGORY MODEL
        model = Category



class BookSerializer (serializers.ModelSerializer):

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
            'created_on'
        )     
        model = Book 



class ProductSerializer(serializers.ModelSerializer):

    class meta:
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'description',
            'quantity',
            'created_on',
            'img_url',
            'status'
        )

        model = Product