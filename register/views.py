from django.shortcuts import render, redirect
from .forms import RegistrationModel
 
 
# Create your views here.
def register(request):
    context = {"form":RegistrationModel}
    return render(request, "index.html", context)
 
def addUser(request):
    modelform = RegistrationModel(request.POST)
    if modelform.is_valid():
        modelform.save()
    return redirect('register')