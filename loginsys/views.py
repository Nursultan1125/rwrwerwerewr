from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.urls import reverse

from cart.cart import Cart
from footer_data.models import TitleFooter
from loginsys.forms import UserCreateProfile, UserPasswordChange
from orders.models import Order, OrderItem
from product.models import Category


def login(request):
    args = dict()
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['error_login'] = "Вы ввели не правильный логин или пороль"
            return render(request, "loginsys/login.html", args)
    else:
        return render(request, "loginsys/login.html", args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = dict()
    args.update(csrf(request))
    return render(request, "loginsys/register.html", args)


def password_chage(request):
    args = dict()
    args.update(csrf(request))
    if request.user.is_anonymous():
        return redirect('/')
    if request.POST:
        new_pass_ch = UserPasswordChange(user=request.user, data=request.POST)
        if new_pass_ch.is_valid():
            new_pass_ch.save()
            update_session_auth_hash(request, new_pass_ch.user)
            return redirect('/user/password_change/done/')
    else:
        args['form'] = UserPasswordChange(request.user)
    return render(request, "registration/password_change_form.html", args)


def password_chage_done(request):
    return render(request, 'registration/password_change_done.html')


def personal_area(request):
    orders = Order.objects.filter(users_id=auth.get_user(request).id)
    data = {
        'orders': orders,
    }
    return render(request, 'loginsys/personal_area.html', data)