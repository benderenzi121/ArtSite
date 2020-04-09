from django.contrib import admin
from django.conf.urls import url
from django.urls import re_path
from django.urls import path
from users.views import help
from django.conf.urls import include

urlpatterns = [
    re_path(r'/help' , help , name = help)
    
    ]