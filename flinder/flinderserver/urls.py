from django.contrib import admin
from django.urls import path, include
from flinderserver import views
from flinderserver import api

app_name = "flinder"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('register/account_type', views.register_account_type, name="register_account_type"),
    path('register/room_seeker', views.register_room_seeker, name="register_room_seeker"),
    path('register/room_provider', views.register_room_provider, name="register_room_provider"),
    path('upload_photos', views.upload_photos, name="upload_photos"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('main', views.main, name="main"),
    path('profile/<slug:profile_slug>', views.profile, name="profile"),
    path('api/get_matches', views.get_matches, name="get_matches")
    path('api/get_match', api.get_match, name="get_match")
]
