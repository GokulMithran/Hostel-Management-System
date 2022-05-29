from asyncio.windows_events import NULL
from distutils.command.upload import upload
from pickle import NONE, TRUE
from typing import TypeVar
from unicodedata import name
from django.db import models
import sys
from typing import Any, Iterable, Optional, Set, Tuple, Type, TypeVar, Union
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser as AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager as BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.base import Model
from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location='pics')
# Create your models here.
class students(models.Model):
    #plf_no      =models.CharField(max_length=10,blank=TRUE,default=None)
    first_name  =models.CharField(max_length=100,blank=TRUE,default=None)
    last_name   =models.CharField(max_length=100,blank=TRUE,default=None)
    username    =models.CharField(max_length=100,blank=TRUE,default=None)
    img         =models.ImageField(upload_to='',blank=TRUE,default=None)
    dob         =models.CharField(max_length=10,blank=TRUE,default=None)
    password   =models.CharField(max_length=100,blank=TRUE,default=None)
    email       =models.EmailField(blank=TRUE,default=None)
    phone_no    =models.CharField(max_length=10,blank=TRUE,default=None)
    state       =models.CharField(max_length=100,blank=TRUE,default=None)
    district    =models.CharField(max_length=100,blank=TRUE,default=None)
    address     =models.TextField(blank=TRUE,default=None)
    pincode     =models.CharField(max_length=100,blank=TRUE,default=None)
    fathername  =models.CharField(max_length=100,blank=TRUE,default=None)
    mothername  =models.CharField(max_length=100,blank=TRUE,default=None)
    guardianname=models.CharField(max_length=100,blank=TRUE,default=None)
    parent_no   =models.CharField(max_length=10,blank=TRUE,default=None)
    parent_email=models.EmailField(blank=TRUE,default=None)
    room_no     =models.CharField(max_length=20,blank=TRUE,default=None)
    student_user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,default=None)

class complaints(models.Model):
     doc         =models.CharField(max_length=100,blank=TRUE,default=None)
     username    =models.CharField(max_length=100,blank=TRUE,default=None)
     room_no     =models.CharField(max_length=20,blank=TRUE,default=None)
     desc     =models.TextField(blank=TRUE,default=None)
     student_user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,default=None)

class duplicates(models.Model):
     doc         =models.CharField(max_length=100,blank=TRUE,default=None)
     username    =models.CharField(max_length=100,blank=TRUE,default=None)
     room_no     =models.CharField(max_length=20,blank=TRUE,default=None)
     desc     =models.TextField(blank=TRUE,default=None)
     student_user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,default=None)

