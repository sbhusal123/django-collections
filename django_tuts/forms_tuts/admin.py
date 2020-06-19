from django.contrib import admin
from .models import Products, Order, OrderItem

# Register Your Models Here
admin.site.register(Products)
admin.site.register(OrderItem)
admin.site.register(Order)
