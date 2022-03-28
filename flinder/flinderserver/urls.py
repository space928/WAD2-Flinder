from django.contrib import admin
from django.urls import path, include
from flinderserver import views
from flinderserver import api

app_name = "flinder"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('profile/edit', views.edit_profiles, name="edit_profile"),
    path('register/account_type', views.register_account_type, name="register_account_type"),
    path('register/room_seeker', views.register_room_seeker, name="register_room_seeker"),
    path('register/room_provider', views.register_room_provider, name="register_room_provider"),
    path('upload_photos', views.upload_photos, name="upload_photos"),
    path('main', views.main, name="main"),
    path('profile/<slug:profile_slug>', views.profile, name="profile"),
    path('api/get_cards', api.get_cards, name="get_cards"),
    path('api/get_matches', api.get_matches, name="get_matches"),
    path('api/register_swipe', api.register_swipe, name="register_swipe")
]
