from django.conf.urls import url
from cart import views as cart_view


urlpatterns = [
    url(r'^$', cart_view.cart_detail, name='cart_detail'),
    url(r'^remove/(?P<product_id>\d+)/$', cart_view.cart_remove, name='cart_remove'),
    url(r'^add/(?P<product_id>\d+)/$', cart_view.card_add, name='cart_add'),
    url(r'^add_index/(?P<product_id>\d+)/$', cart_view.card_add_index, name='cart_add_index'),

]

