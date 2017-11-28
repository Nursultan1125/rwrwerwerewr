from django.contrib import auth, messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import message
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.decorators.http import require_POST
from cart.cart import Cart
from cart.forms import CardAddProductForm
from footer_data.models import TitleFooter
from loginsys.forms import UserCreateProfile
from product.models import Product, Category


@require_POST
def card_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form_cart = CardAddProductForm(request.POST)
    if form_cart.is_valid():
        cd = form_cart.cleaned_data
        if product.product_stock < cd['count_product']:
            messages.add_message(request, messages.INFO, 'Извините на складе только %d штук' % product.product_stock)
            return redirect('cart:cart_detail')
        cart.add_product(product=product, count_product=cd['count_product'],
                         update_count=cd['update_product'])
    return redirect('cart:cart_detail')


def card_add_index(request, product_id):
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        try:
            if product.product_stock == 0:
                messages.add_message(request, messages.INFO, "Нет в наличие")
                return redirect('cart:cart_detail')
            if cart.cart[str(product_id)]['count_product'] >= product.product_stock:
                messages.add_message(request, messages.INFO, 'Извините на складе только %d штук' % product.product_stock)
                return redirect('cart:cart_detail')
        except KeyError:
            pass
        cart.add_product(product=product)
        # cart.cart[str(product.id)]['count_product'] += 1
    except ObjectDoesNotExist:
        raise Http404

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_count_form'] = CardAddProductForm(
            initial={
                'count_product': item['count_product'],
                'update_product': True
            })
    return render(request, 'cart/cart_detail.html')
