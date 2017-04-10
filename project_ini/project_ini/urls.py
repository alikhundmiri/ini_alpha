from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import (login_view, logout_view, register_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^job/', include('Job.urls', namespace="jobs")),
    url(r'^library/', include('library.urls', namespace='library')),
    url(r'^photos/', include('mainpage.urls')),
    url(r'^matrimonial/', include('matrimonial.urls', namespace='matrimonial')),
    url(r'^blogs/', include('posts.urls', namespace="blogs")),
    url(r'^qna/', include('questionnaire.urls', namespace="qna")),

    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^register/', register_view, name="register"),
    url(r'^', include('mainpage.urls')),
    # url('^markdown/', include('django_markdown.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)