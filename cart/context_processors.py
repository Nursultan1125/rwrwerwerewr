from cart.cart import Cart


def getting_cart_info(request):
    cart = Cart(request)
    return locals()


