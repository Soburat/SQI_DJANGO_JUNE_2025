from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('album/', views.list_of_album, name="album"),
    path('artist/', views.artists_list, name="artist")
]
    