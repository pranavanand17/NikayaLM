from django.contrib import admin
from . import views
from django.urls import path

urlpatterns=[
    path('register/',views.register,name='register'),
    path('',views.homepage,name='homepage'),
]
