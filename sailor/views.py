from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from sailor.models import students

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")    

def user(request):
          details=students.objects.filter(username=request.user)
          return render(request,"user.html",{'details':details})  
def admin1(request):
    return render(request,"admin1.html")

def update(request):
          details=students.objects.filter(username=request.user)
          return render(request,"user.html",{'details':details})              

def login1(request):
          return render(request,"login1.html")

def logout(request):
        auth.logout(request)
        return redirect('/')
    
def complaint(request):
    return render(request,"cuser.html")
    # return render(request,"index.html",{'dests':dests}) 
def clogin(request):
    return render(request,"clogin.html")       