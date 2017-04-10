from django.contrib import admin
from .models import books
from .models import genre

admin.site.register(books)
admin.site.register(genre)
