from rest_framework.serializers import ModelSerializer, Serializer
from . models import Category, Product

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductListSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category']

class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1