from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate
# Create your views here.
def login(request):
    form = LoginForm(request.POST)
  
    if request.method == "POST":
         if form.is_valid():
            return render (request,'login.html',{'form':form,'error':form.errors.items})
    else:
        form =LoginForm()
    return render (request,'login.html',{'form':form})