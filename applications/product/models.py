# third-party
# Django
from unicodedata import category
from django.db import models
# local

class Category(models.Model):
    """
        Category
    """

    name = models.CharField(
        'Nombre', 
        max_length=30
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Provider(models.Model):
    """
        Provider
    """

    name = models.CharField(
        'Razon Social', 
        max_length=100
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefonos',
        max_length=40,
        blank=True,
    )
    web = models.URLField(
        'sitio web',
        blank=True,
    )


    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
        Product
    """
    
     
    # GENDER
    MEN = 'M'
    WOMAN = 'W'
    OTHER = 'O'
    
    GENDER_CHOICES = [
        (MEN, 'Man'),
        (WOMAN, 'Woman'),
        (OTHER, 'Otro'),
    ]

    

    
    name = models.CharField(
        'Nombre', 
        max_length=250
    )
    provider = models.ForeignKey(
        Provider, 
        related_name='providers',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    image1 = models.ImageField(
        'Imagen 1', 
        blank=True, 
        null=True, 
        upload_to='producto'
    )
    

    due_date = models.DateField(
        'fehca de vencimiento',
        blank=True, 
        null=True
    )
    description = models.TextField(
        'product description',
        blank=True,
    )
    
    
    sale_price = models.DecimalField(
        'price sale',
        max_digits=7, 
        decimal_places=2
    )
    
    anulate = models.BooleanField(
        'delete',
        default=False
    )

    #

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name + '------------' +  str(self.image1)




