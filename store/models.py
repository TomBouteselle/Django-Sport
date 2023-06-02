from django.shortcuts import render
from django.db import models

from projetSport.settings import AUTH_USER_MODEL

# Create your views here.
"""
Product

- Nom
- Prix  
- Quantité en stock
- Description
- Image

"""
class Product(models.Model):
    nom = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return self.nom

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"