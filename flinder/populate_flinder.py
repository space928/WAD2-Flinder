#!/usr/bin/env python
import json
import os
import random

import django

from Data import Get_data

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flinder.settings')
django.setup()
from flinderserver.models import UserProfile, Pictures, Swipe

from django.contrib.auth.models import User


def populate():
    with open("test/flinderTestData.json", "r", encoding="utf-8") as f:
        users = json.loads(f.read())
    with open("test/flinderTestImages.json", "r", encoding="utf-8") as f:
        images = json.loads(f.read())
    for data in users:
        user = add_user(data)
        data["username"] = user
        add_user_profile(data, user)
        image = random.choice(images)
        add_picture(user, image["picture"], image["description"])
    for i in range(100):
        add_random_swipe(users)
    

def add_random_swipe(users):
    user1 = random.choice(users)["username"].id
    user2 = random.choice(users)["username"].id
    swipe = random.choice([True,False])
    new_swipe = Swipe.objects.get_or_create(
        swiped_id=user1, 
        swiper_id=user2,
        swipeRight=swipe)[0]
    return new_swipe


def add_picture(user, picture, description):
    new_picture = Pictures.objects.get_or_create(poster=user)[0]
    new_picture.picture = picture
    new_picture.description = description
    new_picture.save()
    return new_picture


def add_user(user):
    user = User.objects.get_or_create(username=user["username"])[0]
    user.save()
    return user


def add_user_profile(user_profile, OriginalUser):
    new_user = UserProfile()
    for key in user_profile:
        setattr(new_user, key, user_profile[key])

    print(user_profile["name"])
    new_user.save()

    return new_user


if __name__ == '__main__':
    print('Starting flinder population script...')
    populate()
