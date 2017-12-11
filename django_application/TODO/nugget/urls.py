from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^nugget$', views.nugget, name='nugget'),
    url(r'^shop$', views.shop, name='shop'),
    url(r'^community$', views.community, name='community'),
    url(r'^battle$', views.battle, name='battle'),
    url(r'^create$', views.create, name='create'),
    url(r'^help$', views.help, name='help'),
    url(r'^myaccount$', views.myaccount, name='myaccount'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.profile_page, name='profile'),
    url(r'^chat/(?P<id>[a-zA-Z0-9]+)$', views.private_msg, name='private_msg'),
    url(r'^forum/(?P<topic>[a-zA-Z0-9]+)$', views.forum, name='forum'),
    url(r'^forum/(?P<topic>[a-zA-Z0-9]+)/(?P<id>[a-zA-Z0-9]+)$', views.forum_post, name='forum_post'),
    url(r'^hidden$', views.hidden, name='hidden'),
    url(r'^testview$', views.testview, name='testview'),
]


from django.conf.urls import (handler400, handler403, handler404, handler500)

handler400 = 'nugget.views.bad_request'
handler403 = 'nugget.views.permission_denied'
handler404 = 'nugget.views.page_not_found'
handler500 = 'nugget.views.server_error'
