from dataclasses import field
from rest_framework import serializers      #TO SERIALIZE A DATA TO A JSON FORMAT
from .models import *
from django.contrib.auth.models import User


#   FOR REGISTRING OUR USER
class RegistrationSerializer(serializers.ModelSerializer):

    # TO OVERRIDE THE FIELDS 
    email = serializers.EmailField(min_length = 5)
    username = serializers.CharField(max_length = 30)
    password = serializers.CharField(min_length = 4, write_only = True)

    class Meta:
        fields = ('first_name', 'last_name', 'id', 'email', 'username', 'password')
        model = User     # FROM INBUILT JWT AUTH

    #  QUERY TO VALIDATE DATA FROM USER
    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ( 'email already exists' )})        #ERROR MSG
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ( 'username, already exists' )})    

        return super().validate(args)  


    #  CREATE USER USING THE VALID INFO
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)      




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
        fields = (         # FOR THE USER MODEL
            'id',
            'username',
            'email',
            'books',
            'products'
        )

        model = User     # FROM DJANGO AUTH MODELS



class CartUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username',
            'email',
            'books',
            'products',
            'id'
        )

        model = User     # FROM DJANGO AUTH MODELS


#CART SERIALIZER
class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True, many=False)
    books = BookSerializer(read_only=True, many=True)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        fields = (
            'cart_id',
            'created_at',
            'products',
            'books'
        )
        # specific model
        model = Cart
