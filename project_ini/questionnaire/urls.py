from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$', views.qna_list, name='list'),
    url(r'^create/$', views.qna_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.qna_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.qna_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.qna_delete, name='delete'),

]
