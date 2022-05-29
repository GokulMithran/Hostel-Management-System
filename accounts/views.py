from asyncio.windows_events import NULL
import email
from email.policy import default
from multiprocessing import AuthenticationError
from multiprocessing.reduction import duplicate
from pyexpat.errors import messages
from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User, auth
from contextlib import redirect_stderr
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages

import json
from urllib.request import urlopen
import os
from django.utils.translation import gettext_lazy as _
# from mini.sailor.models import complaints
# from mini.sailor import admin
from sailor.models import students ,complaints ,duplicates
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
#from mini.sailor import admin
# Create your views here.

# def register(request):
#     pass
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("user")

        else:
            messages.info(request,'Wrong Username & Password')
            return redirect("login")

    else:
        
        return render(request,'login.html')

def logout(request):
        auth.logout(request)
        return redirect('/')

def register(request):

    if request.method=='POST':
        room_no=request.POST['room_no']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        img=request.FILES['img']
        dob=request.POST['dob']
        state=request.POST['state']
        district=request.POST['district']
        address=request.POST['address']
        pincode=request.POST['pincode']
        fathername=request.POST['fathername']
        mothername=request.POST['mothername']
        guardianname=request.POST['guardianname']
        parent_no=request.POST['parent_no']
        parent_email=request.POST['parent_email']

        if password1==password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return HttpResponseRedirect(reverse('register'))
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email Taken')
                 return redirect('register')      
            else:
                user1=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)    
                user=students(first_name=first_name,last_name=last_name,username=username,dob=dob,email=email,password=password1,phone_no=phone_no,img=img,state=state,district=district,address=address,pincode=pincode,fathername=fathername,mothername=mothername,guardianname=guardianname,parent_no=parent_no,parent_email=parent_email,room_no=room_no,student_user=user1)
                user1.save();
                user.save();
                print('User created')
                return redirect('login')

    else:
        return render(request,'register.html')

def user(request):
          details=students.objects.filter(username=request.user)
          return render(request,"user.html",{'details':details})

def update(request):
    # u=students.objects.get(email=email)
    if request.method=='POST':
        # plf_no=request.POST['plf_no']
        # username = request.GET['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        # img=request.FILES['img']
        dob=request.POST['dob']
        state=request.POST['state']
        district=request.POST['district']
        address=request.POST['address']
        pincode=request.POST['pincode']
        fathername=request.POST['fathername']
        mothername=request.POST['mothername']
        guardianname=request.POST['guardianname']
        parent_no=request.POST['parent_no']
        parent_email=request.POST['parent_email']
           
    
    user1=students.objects.filter(username=request.user)
    a=students.objects.get(username=request.user)
    print(a)
    
    for i in user1:
    # username=user1.username

        if(first_name!=i.first_name):
            user1.update(first_name=first_name)
        if(last_name!=i.last_name):
            user1.update(last_name=last_name)
        if(phone_no!=i.phone_no):
            print(i.phone_no)
            user1.update(phone_no=phone_no)
        if(dob!=i.dob):
            user1.update(dob=dob) 
        # if(img!=NULL):
        #     user1.update(img=img)
        if(state!=i.state):
            user1.update(state=state)
        if(district!=i.district):
            user1.update(district=district)
        if(address!=i.address):
            user1.update(address=address)
        if(pincode!=i.pincode):
            user1.update(pincode=pincode)
        if(fathername!=i.fathername):
            user1.update(fathername=fathername)
        if(mothername!=i.mothername):
            user1.update(mothername=mothername) 
        if(guardianname!=i.guardianname):
            user1.update(guardianname=guardianname)                
        if len(request.FILES)==1:
            print(len(request.FILES))
            if len(i.img) > 0:
                os.remove(i.img.path)
                # print("1234")
                i.img = request.FILES['img']
                # os.replace(i.img.path)
                user1.update(img=i.img)
                a.img=request.FILES['img']
                a.save()

    
    print('User Updated')
    details=students.objects.filter(username=request.user)
    return render(request,"user.html",{'details':details})    
    # return render(request,"user.html")
    

def admin1(request):
    details=User.objects.filter(username=request.user)
    return render(request,"admin1.html",{'details':details})     
    #return render(request,'admin1.html')
        

def login1(request):  
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        # return redirect("/")
       # print(user.is_superuser)
        print(user)
        if user is not None:
            if  user.is_superuser :  
                                
            #return render(request,'admin1.html')
                # return redirect("admin1")
                details=students.objects.all()
                return render(request,"admin1.html",{'username':username,'details':details })

            else:
                messages.info(request,'Wrong Username & Password')
                return render(request,'login1.html')
        else:
                messages.info(request,'Wrong Username & Password')
                return render(request,'login1.html')        

    else:
        
        return render(request,'login1.html')                      
    # sreturn render(request,'login1.html')

def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        # if (len(searched)!=0):
        details=students.objects.filter(username__contains=searched)
        return render(request,'admin1.html',{'details':details})
        # elif (len(searched)==0):     
        #      details=students.objects.all()
        #      return render(request,'admin1.html',{'searched':searched,'details':details})

def adminedit(request):
    if request.method=="POST":
        room_no=request.POST['room_no']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        dob=request.POST['dob']
        user1=students.objects.filter(email=email)
        print(user1)
        user=User.objects.filter(email=email)
        for i in user1:
            if(phone_no!=i.phone_no):
                user1.update(phone_no=phone_no)
                print("gokul")
            if(dob!=i.dob):
                user1.update(dob=dob)
                print("gokul")
            if(email!=i.email):
                user1.update(email=email)
            if(room_no!=i.room_no):
                user1.update(room_no=room_no)   
        for i in user:
            if(email!=i.email):
                user.update(email=email)
        
        details=students.objects.all()
        return render(request,"admin1.html",{'details':details})        
        # return redirect("")  
    else:
        return redirect("admin1")          

def delete(request, username):
    user1 = students.objects.get(username=username)
    user = User.objects.get(username=username)
    user1.delete()
    user.delete()
    return HttpResponseRedirect(reverse('admin1'))

def cuser(request):
        details = students.objects.filter(username=request.user)
        print(details)
        return render(request,"cuser.html",{'details':details})

def csend(request):
        user1=User.objects.get(username=request.user)
        if request.method=="POST":
            room_no=request.POST['room_no']
            plf_no=request.POST['plf_no']         
            doc=request.POST['doc']
            desc=request.POST['desc']
            user=complaints(room_no=room_no,username=plf_no,doc=doc,desc=desc,student_user=user1)
            user1=duplicates(room_no=room_no,username=plf_no,doc=doc,desc=desc,student_user=user1)
            user.save()
            user1.save()
            return redirect('/')
def complaint(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if  user.is_superuser :  
                                
            
                details=complaints.objects.all()
                
                return render(request,"complaint.html",{'username':username,'details':details })

            else:
                details = students.objects.filter(username=username)

                return render(request,"cuser.html",{'details':details})
                #return redirect('cuser')
        else:
                messages.info(request,'Wrong Username & Password')
                return render(request,'clogin.html')        

    else:
        
        return render(request,'login1.html')
def clogin(request):
    return render(request,"clogin.html")        

def cdelete(request, id):
    user1 = complaints.objects.get(id=id)
    user1.delete()
    return HttpResponseRedirect(reverse('complaint.html'))