from rest_framework import serializers
from django.contrib.auth.models import User
from mainApp.models  import Flower, Category, UserDetails, Orders, Cart, Wishlist

class flowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "last_login", "is_superuser", "username",  "first_name", "last_name", "email", "is_staff", "date_joined"]

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'



# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = '__all__'

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = '__all__'

# class WishlistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wishlist
#         fields = '__all__'
