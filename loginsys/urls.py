from django.conf.urls import url
from django.contrib import admin
from loginsys import views as login_views


urlpatterns = [
    url(r'^login/$', login_views.login, name='login'),
    url(r'^logout/$', login_views.logout, name='logout'),
    url(r'^register/$', login_views.register, name='register'),
    url(r'^password_change/$', login_views.password_chage, name='password_change'),
    url(r'^password_change/done/$', login_views.password_chage_done, name='password_change_done'),
    url(r'^personal_area/$', login_views.personal_area, name='personal_area'),

]

