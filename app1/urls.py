from django.contrib import admin
from django.urls import path
from django.views.defaults import server_error
from .views import  index_template_app

urlpatterns = [
    path('', index_template_app)
    
    ]
