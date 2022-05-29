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

urlpatterns = [
    # path("admin",views.admin,name="admin"),
    path("user",views.user,name="user"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("admin1",views.admin1,name="admin1"),
    path("update",views.update,name="update"),
    path("login1",views.login1,name="login1"),
    path("logout",views.logout,name="logout"),
    path("search",views.search,name="search"),
    path("adminedit",views.adminedit,name="adminedit"),
    path('delete/<username>', views.delete, name='delete'),
    path("cuser",views.cuser,name="cuser"),
    path("csend",views.csend,name="csend"),
    path("complaint",views.complaint,name="complaint"),
    path("clogin",views.clogin,name="clogin"),
    path('cdelete/<id>', views.cdelete, name='cdelete'),
     

]
