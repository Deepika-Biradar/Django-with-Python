"""
URL configuration for function project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from event import views
from .views import send_email_view

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("login",views.login),
    path("changepassword",views.changepassword),
    path("register",views.register),
    path("registerdata",views.registerdata),
    path("searchregisters",views.searchregisters),
    path("searchregister",views.searchregister),
    path("halldetails",views.halldetails),
    path("savehalldetails",views.savehalldetails),
    path("searchhall",views.searchhall),
    path("food",views.food),
    path("savehalldetails",views.savehalldetails),
    path("savefood",views.savefood),
    path("chairdetails",views.chairdetails),
    path("savechair",views.savechair),
    path("decorationtype",views.decorationtype),
    path("savedecoration",views.savedecoration),
    path("register1",views.register1),
    path("registerdata1",views.registerdata1),
    path("login1",views.login1),
    path("changepasswordA",views.changepasswordA),
    path("saveall",views.saveall),
    path("completeregister",views.completeregister),
    path("nav",views.nav),
    path("home1",views.home1),
    path("imghall",views.imghall),

    path("imgfood",views.imgfood),

    path("imgtheme",views.imgtheme),
    path('send_email_view',views.send_email_view,name="send_email_view"),
    path("home2",views.home2),

    






]
