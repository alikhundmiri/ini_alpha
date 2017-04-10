from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^photos/$', views.photos, name='photos'),
    url(r'^profile/$', views.profile, name='profile'),

]
