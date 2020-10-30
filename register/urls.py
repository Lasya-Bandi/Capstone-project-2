from django.urls import path
from .views import register, addUser
 
urlpatterns = [
    path('', register, name = "register"),
    path('add/', addUser, name = "addUser"),
 
]