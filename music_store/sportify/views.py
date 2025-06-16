from django.shortcuts import render
from .models import Album,Artist

# Create your views here.
def home(request):
    return render(request, "sportify/homepage.html")

def list_of_album(request):
    albums = Album.objects.all().order_by('release_date')
    return render(request, "sportify/album.html", {'albums': albums})

def artists_list(request):
    artists = Artist.objects.all().order_by('debut_year')
    return render(request, "sportify/artist.html", {'artists': artists})