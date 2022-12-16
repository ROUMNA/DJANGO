"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from .views import index, page, index_template
from app1.views import *

urlpatterns = [
    url("page/", model_view, name= "model"),
    url("python_profil", python_profil , name = "python"),
    url("datascience", data_science , name = "datascience"),
    url("trainer", trainer_profil , name = "trainerprofil"),

    url("", page_acceuil, name = "home") 
    ]
