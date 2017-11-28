from django.conf.urls import url
from search import views as search_view

urlpatterns = [

    url(r'^$', search_view.seach, name='search'),


]