from itertools import product
from rest_framework import viewsets
from .models import (Category, Provider, Product)
from .serializers import(ProductSerializer, CategorySerializer, ProviderSerializer, PaginationSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    
    
class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    
    
    
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = PaginationSerializer
    
    def get_queryset(self):
        product = Product.objects.filter(anulate=False)

        return product
    