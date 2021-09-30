from django.contrib import admin
from django.urls import path
from projectSite import views

urlpatterns = [
    path("", views.index, name = 'projectSite'),
    path("user/", views.userFunc, name = 'userInfo'),
]
