from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "Library/home.html")

def book_list(request):
    return render(request,"Library/list-of-books.html")