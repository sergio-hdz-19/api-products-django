from rest_framework import serializers, pagination
from rest_framework.response import Response

from .models import (Category, Provider, Product)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    proveedor = serializers.CharField(source='provider.name', read_only=True)
    categoria = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'provider',
            'category',
            'image1',
            'description',
            'sale_price',
            'proveedor',
            'categoria'
        )


class PaginationSerializer(pagination.PageNumberPagination):
        page_size = 8
        max_page_size = 50

    
        


