from django.shortcuts import render, HttpResponse

# Create your views here.
def about_us (request):
    return HttpResponse ('Here, we sell quality household gadgets')