from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
# from Job.models import job_detail


urlpatterns = [
    # /lobrary/
    url(r'^$', views.index, name='books_list'),
    # /library/book_id
    url(r'^(?P<book_id>\d+)$', views.detail, name='book_info'),
    # /library/genre/genre_id
    url(r'^genre/(?P<genre_id>[-\w]+)/', views.genre, name='genre_details'),
]

