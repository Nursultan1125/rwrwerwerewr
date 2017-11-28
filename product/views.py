from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf

from cart.cart import Cart
from cart.forms import CardAddProductForm
from comments.models import Comment
from footer_data.models import TitleFooter
from loginsys.forms import UserCreateProfile
from product.models import Product, Category
from django.contrib import auth


def index(request):
    products = Product.objects.filter(is_public=True).order_by('-product_date_update')
    carrent_page = Paginator(products, 21)
    data = {
        'products': carrent_page.page(1),
    }

    data.update(csrf(request))
    return render(request, 'product/index.html', data)


def get_product(request, id):
    cart_product_form = CardAddProductForm()
    data = {
        'product': get_object_or_404(Product, id=id),
        'comments': Comment.objects.filter(comment_product_id=id),
        'cart_product_form': cart_product_form,

    }
    data.update(csrf(request))
    return render(request, 'product/product.html', data)


def get_category(request, slug):
    category = Category.objects.get(category_slug=slug)
    category_parent = Category.objects.filter(category_parent=None)
    category_chaild = [i for i in Category.objects.all() if i.category_parent in category_parent]
    category_chaild_not = [i for i in category_parent for j in category_chaild if i == j.category_parent]
    category_chailds = [i for i in category_chaild if category == i.category_parent]
    products = list()
    for i in category_chailds:
        products += i.get_product()
    products += category.get_product()
    data = {
        'products': products,
        'category': category,
        'categorys': category_parent,
        'category_chaild': category_chaild,
        'category_chaild_not': category_chaild_not,
    }

    data.update(csrf(request))
    return render(request, 'product/category.html', data)



