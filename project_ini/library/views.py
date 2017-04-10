from django.shortcuts import render
from django.http import Http404
from .models import books, genre

def index(request):
    book_list = books.objects.all()
    return render(request, 'library/library_index.html', {'book_list': book_list})

def detail(request, book_id):
    try:
        this_book = books.objects.get(pk = book_id)
    except books.DoesNotExist:
        raise Http404('Book Does not Exist!')
    return render(request, 'library/library_detail.html',{'this_book': this_book})

def genre(request, genre_id):
    try:
        check = genre.objects.get(pk = genre_id)
    except genre.DoesNotExist:
        raise Http404('This genre Doe not Exist!')
    these = books.objects.get(genre = genre_id)
    return render(request, 'library/library_genre.html', {'these': these})