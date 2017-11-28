from django.shortcuts import render, redirect

# Create your views here.
from comments.models import Comment
from product.models import Product


def create_comment(request, id):
    product = Product.objects.get(id=id)
    c = Comment(
        comment_body=request.GET.get('body', 'No text'),
        comment_author=request.user,
        comment_product=product
    )
    c.save()
    return redirect('/product/%s/' % product.id)
