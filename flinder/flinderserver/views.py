from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms.models import model_to_dict

from flinderserver.forms import RoomSeekerForm, RoomProviderForm, UserForm, UserProfileForm
from flinderserver.models import UserProfile, Pictures, Swipe


# Create your views here.
def index(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {}

    # Render the web page
    response = render(request, "flinder/index.html", context=context_dict)

    return response


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('flinder:main'))
            else:
                return HttpResponse("Your Flinder account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("invalid login details supplied.")
    else:
        return render(request, 'flinder/login.html')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect(reverse('flinder:register_account_type'))
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'flinder/register.html', context={'user_form': user_form})


@login_required
def edit_profiles(request):
    registered = False
    # This should get from profiles:  request.user
    user_profile = UserProfile.objects.get(pk=1)
    print(user_profile)
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect(reverse('flinder:register_account_type'))
        else:
            print(user_form.errors)
    else:
        user_form = UserProfileForm(request.POST, instance=user_profile, initial=model_to_dict(user_profile))
    return render(request, 'flinder/edit_profile.html', context={'user_form': user_form})


@login_required
def register_account_type(request):
    return render(request, "flinder/register_account_type.html")


@login_required
def register_room_seeker(request):
    # Query the database for any data needed to build the page
    if request.method == 'POST':
        room_seeker_form = RoomSeekerForm(request.POST)
        if room_seeker_form.is_valid():
            # Save the form making sure to populate the flatSearcher and username fields
            room_seeker = room_seeker_form.save(commit=False)
            room_seeker.username = request.user
            room_seeker.flatSearcher = True
            room_seeker.save()

            return redirect(reverse('flinder:upload_photos'))
        else:
            print(room_seeker_form.errors)
    else:
        room_seeker_form = RoomSeekerForm()

    # Context for the html template
    context_dict = {
        'room_seeker_form': room_seeker_form
    }

    # Render the web page
    response = render(request, "flinder/register_room_seeker.html", context=context_dict)

    return response


@login_required
def register_room_provider(request):
    # Query the database for any data needed to build the page

    if request.method == 'POST':
        room_provider_form = RoomProviderForm(request.POST)
        if room_provider_form.is_valid():
            # Save the form making sure to populate the flatSearcher and username fields
            room_provider = room_provider_form.save(commit=False)
            room_provider.username = request.user
            room_provider.flatSearcher = False
            room_provider.save()

            return redirect(reverse('flinder:upload_photos'))
        else:
            print(room_provider_form.errors)
    else:
        room_provider_form = RoomProviderForm()

    # Context for the html template
    context_dict = {
        'room_provider_form': room_provider_form
    }

    # Render the web page
    response = render(request, "flinder/register_room_provider.html", context=context_dict)

    return response


# @login_required
def upload_photos(request):
    current_images = Pictures.objects.filter(poster=request.user)
    context_dict = {'images': [img.picture.url for img in current_images]}

    if request.method == 'POST':
        # Check each image is of an appropriate type
        for image in request.FILES.values():
            if image.content_type != "image/jpeg" and image.content_type != "image/png":
                context_dict['msg'] = "Img type forbidden! Please upload an img"
                return render(request, "flinder/upload_photos.html", context=context_dict)

        # Save each image to the DB
        for image in request.FILES.values():
            print(f"Uploading {image.name}...")
            img = Pictures(picture=image, description=image.name, poster=request.user)
            img.save()

        context_dict['msg'] = "Upload success!"
        return render(request, "flinder/upload_photos.html", context=context_dict)

    return render(request, 'flinder/upload_photos.html', context=context_dict)


@login_required
def main(request):
    # Render the web page
    response = render(request, "flinder/main.html")

    return response


@login_required
def profile(request, profile_slug):
    # Query the database for any data needed to build the page
    try:
        db_profile = UserProfile.objects.get(uuid=profile_slug)
    except UserProfile.DoesNotExist:
        db_profile = None

    # If the profile doesn't exist, redirect the user to the main page
    if db_profile is None:
        return redirect('flinder:main')

    # Context for the html template
    context_dict = {
        "profile": db_profile,
    }

    # Render the web page
    response = render(request, "flinder/profile.html", context=context_dict)

    return response
