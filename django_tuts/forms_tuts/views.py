from django.shortcuts import render
from django.http import HttpResponse

from .forms import OrderForm
from django.views.generic import FormView


class OrderView(FormView):
    """View to render the order form"""
    form_class = OrderForm
    template_name = 'order.html'
