from django.shortcuts import redirect
from django.urls import path
from app import views

urlpatterns = [
    path("login/", views.login,name = "login"),
    path('register/', views.register,name = 'register'),
    path('logOut/', views.logOut,name = 'logOut'),
    path('chargeSelfInfo/', views.chargeSelfInfo, name='chargeSelfInfo'),
    path("home/",views.home,name = "home"),
]
