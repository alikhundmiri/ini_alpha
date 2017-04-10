from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$', views.job_list, name='list'),
    url(r'^create/$', views.job_create, name='create'),
    url(r'^(?P<slug>[\w-]+)$', views.job_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.job_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.job_delete, name='delete'),
]
