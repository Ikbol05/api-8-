from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics
from . serializers import CategorySerializer, ProductListSerializer, ProductDetailSerializer
from . models import Category, Product
from rest_framework.authtoken.models import Token
from  rest_framework.decorators import api_view
from rest_framework.response import Response


class CategoryCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductCreateView(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

@api_view(['POST'])
def login(request):
    username = request.data('username')
    password = request.data('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token = Token.objects.get_or_create(user=user)
        context = {
            'success': True,
            'username': user.username,
            'key': token.key
        }
    else:
        context = {
            'success': False
        }

    return Response(context)
