from django.urls import path

from . import views

urlpatterns = [
    path ('profile_app/', views.index, name='index'),
    path ('profile_app/', views.hobbies, name='hobbies'),
    path ('profile_app/', views.goals, name='goals'),
    
]