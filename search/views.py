from django.contrib import auth
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from cart.cart import Cart
from loginsys.forms import UserCreateProfile
from product.models import Product, Category
from search.search import get_query


def seach(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        entry_query = get_query(query, ['product_name', 'product_overview_anons', ])
        product = Product.objects.filter(entry_query).order_by('-product_date_create')
        data = {
            'products': product,
            'query': query,
        }
        data.update(csrf(request))

        return render(request, 'search/search.html', data)
    else:
        return redirect('/')
