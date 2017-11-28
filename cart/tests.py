from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.test import TestCase

from cart.cart import Cart
from product.models import Product
