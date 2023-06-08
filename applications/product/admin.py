from django.contrib import admin
from .models import (Category, Provider, Product)
# Register your models here.

admin.site.register(
    {
        Category,
        Provider,
        Product
    }
)
