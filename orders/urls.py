from django.conf.urls import url
from orders import views as order_view


urlpatterns = [

    url(r'^create/$', order_view.order_create, name='order_create'),


]

