from django.shortcuts import render
from.models import Author
# Create your views here.
from library.models import Book

def all_authors(request):
    return render(request, "Authors/authors.html")

def book_signings(request):
    return render(request, "Authors/book-signings.html")

def mvt(request):
    author_info = Author.objects.order_by("birth_date")
    authors= Author.objects.all()
    book_info = Book.objects.order_by("-title") #descending order

    context = {
        "author_dob" : author_info, 
        "books" : book_info,
        "authors" : authors,

    }
    return render(request, "Authors/mvt.html", context)