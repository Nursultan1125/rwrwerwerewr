"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from comments.views import create_comment
from product import views as product_views
from product import urls as product_urls
from loginsys import urls as login_urls
from cart import urls as cart_urls
from orders import urls as order_urls
from search import urls as searh_urls
from footer_data import views as footer_data_views


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),
    url(r'^product/', include(product_urls, namespace='product')),
    url(r'^category/(?P<slug>\w+)/', product_views.get_category, name='get_category'),
    url(r'create_comment/(?P<id>\d+)/$', create_comment, name='create_comment'),
    url(r'^auth/', include(login_urls, namespace='auth')),
    url(r'^user/', include(login_urls, namespace='user')),
    url(r'^cart/', include(cart_urls, namespace='cart')),
    url(r'^order/', include(order_urls, namespace='orders')),
    url(r'^search/', include(searh_urls, namespace='search')),
    url(r'^$', product_views.index, name="index"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^delivery/', footer_data_views.get_delivery, name='delivery'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)