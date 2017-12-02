from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^nugget$', views.nugget, name='nugget'),
    url(r'^shop$', views.shop, name='shop'),
    url(r'^chat$', views.chat, name='chat'),
    url(r'^battle$', views.battle, name='battle'),
    url(r'^create$', views.create, name='create'),
    url(r'^help$', views.help, name='help'),
]
