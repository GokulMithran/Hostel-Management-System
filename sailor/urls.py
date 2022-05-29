"""mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin 
from django.urls import path
from.import views
from re import template
from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",views.index,name="index"),
    path("",views.login,name="login"),
    path("",views.user,name="user"),
    path("",views.admin1,name="admin1"),
    path("",views.update,name="user"),
    path("",views.login1,name="login1"),
    path("",views.logout,name="logout"),
    path("",views.complaint,name="complaint"),
    path("",views.clogin,name="clogin"),


]
# urlpatterns =urlpatterns +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
