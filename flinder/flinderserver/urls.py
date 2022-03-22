from django.contrib import admin
from django.urls import path, include
from flinderserver import views
from flinderserver.api import get_match

app_name = "flinder"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('register/account_type', views.register_account_type, name="register_account_type"),
    path('register/room_seeker', views.register_room_seeker, name="register_room_seeker"),
    path('register/room_provider', views.register_room_provider, name="register_room_provider"),
    path('main', views.main, name="main"),
    path('api/get_match',get_match)
]
