"""
URL configuration for praveen project.

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
from insta.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',HOME,name='index'),
    path('name/',SAM,name='sam'),
    path('new/',TEMP1,name='temp'),
    path('register/',REGISTER,name='register'),
    path('user_login/',USER_LOGIN,name='user_login'),
    path('user_logout/',USER_LOGOUT,name='user_logout'),
    path('Sample/',SAMPLE,name='Sample')

]
