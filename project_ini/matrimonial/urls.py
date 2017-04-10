from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$', views.mat_list, name='list'),
    url(r'^create/$', views.mat_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.mat_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.mat_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.mat_delete, name='delete'),
]
