from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "nikky_kitchen/index.html" )

def about(request):
    return render(request, "nikky_kitchen/about.html" )

def contact(request):
    return render(request, "nikky_kitchen/contact.html" )

