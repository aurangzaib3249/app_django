import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from .forms import *
from .models import *
def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(username=email,password=password)
        print("user",user)
        if user:
            user=UserSerilizer(user).data
            request.session["user"]=user
            return redirect("home")
        else:
            request.session["user"]=None
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect("login")
    else:
        form=UserForm()
    return render(request,"register.html",{"form":form})
    
def home(request):
    return HttpResponse("<h1>Home Page</h1>")
    

def logout(request):
    request.session["user"]=None
    return redirect("login")