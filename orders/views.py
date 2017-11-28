from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from cart.cart import Cart
from footer_data.models import TitleFooter
from loginsys.forms import UserCreateProfile
from orders.forms import OrderCreateForm
from orders.models import OrderItem
from orders.tasks import OrderCreated
from product.models import Category


@csrf_exempt
def order_create(request):
    cart = Cart(request)
    if cart.get_total_count() == 0:
        return redirect('cart:cart_detail')
    if not auth.get_user(request).is_authenticated():
        return redirect('auth:register')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print(request.POST)
        if form.is_valid():
            order = form.save()
            order.users = auth.get_user(request)
            order.save()

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['prices'],
                                         count=item['count_product'])
            cart.clear()
            OrderCreated(order.id)

            return render(request, 'orders/order_created.html')

    form = OrderCreateForm()
    args = {
        'cart': cart,
        'form_order': form,
    }
    return render(request, 'orders/order_create.html', args)
