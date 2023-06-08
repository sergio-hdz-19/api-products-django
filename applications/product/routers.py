from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .viewsets import ProductViewSet, CategoryViewSet, ProviderViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('providers', ProviderViewSet, basename='providers')

urlpatterns = [
    path('', include(router.urls)),
]