from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'my_app/welcome.html')