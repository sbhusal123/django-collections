from django import forms
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    """Form to place an order"""

    def __init__(self, *args, **kwargs):
        """Form object innitializer: Construtor"""
        super(OrderForm, self).__init__(*args, **kwargs)

    class Meta:
        """Meta data for form object"""
        model = Order
        fields = ('items', 'total', 'date', 'user')

class OrderItemForm(forms.ModelForm):
    """Form to add an item to an order"""

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')

