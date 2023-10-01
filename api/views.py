from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from mainApp.models import Flower, Category, UserDetails, Orders, Cart, Wishlist
from .serializer import flowerSerializer, categorySerializer, UserSerializer, UserDetailSerializer

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUserDetails(request):
    user_details = UserDetails.objects.all()
    serializer = UserDetailSerializer(user_details, many= True)
    print(serializer)
    return Response(serializer.data)

@api_view(["GET"])
def getFlowers(request):
    flowers = Flower.objects.all()
    serializer = flowerSerializer(flowers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = categorySerializer(categories, many=True)
    return Response(serializer.data)



# @api_view(['GET'])
# def getOrders(request):
#     orders = Orders.objects.all()
#     serializer = categorySerializer(orders, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getCart(request):
#     cart = Cart.objects.all()
#     serializer = categorySerializer(cart, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getWishlist(request):
#     wishlist = Wishlist.objects.all()
#     serializer = categorySerializer(wishlist, many=True)
#     return Response(serializer.data)