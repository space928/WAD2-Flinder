from django.contrib import admin
from django.urls import path, include
from flinderserver import views

app_name = "flinder"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]
