from django.contrib import auth
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf

from cart.cart import Cart
from footer_data.models import TitleFooter, Delivery
from loginsys.forms import UserCreateProfile
from product.models import Category


def get_delivery(request):
    delivery = Delivery.objects.all()
    products = list()
    data = {
        'products': products,
        'delivery': delivery,
    }
    data.update(csrf(request))
    return render(request, 'delivery/get_delivery.html', data)