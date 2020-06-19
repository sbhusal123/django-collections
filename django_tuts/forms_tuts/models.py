from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Products(models.Model):
    """Products for sale"""
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class OrderItem(models.Model):
    """Item collection in a order"""
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

class Order(models.Model):
    """Order information"""
    items = models.ManyToManyField('OrderItem')
    total = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)