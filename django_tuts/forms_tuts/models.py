from _datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Products(models.Model):
    """Products for sale"""
    name = models.CharField(max_length=256, unique=True, null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name}: {self.price}'

class OrderItem(models.Model):
    """Item collection in an order"""
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=False, null=False)  # validate such that no less than 3

class Order(models.Model):
    """Order information"""
    items = models.ManyToManyField('OrderItem')
    date = models.DateTimeField(default=datetime.now, blank=False)  # validate such that not yesterday
    total = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)