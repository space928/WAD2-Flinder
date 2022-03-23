from django.shortcuts import render
from flinderserver.forms import RoomSeekerForm, RoomProviderForm
from flinderserver.models import UserProfile, Pictures, InterestsAndPriorities, Swipe
from flinderserver.forms import UserForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {}

    # Render the web page
    response = render(request, "flinder/index.html", context=context_dict)

    return response


def login(request):
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
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect(reverse('flinder:register_account_type'))
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'flinder/register.html',context = {'user_form': user_form})


def register_account_type(request):
    return render(request, "flinder/register_account_type.html")


def register_room_seeker(request):
    # Query the database for any data needed to build the page
    if request.method == 'POST':
        room_seeker_form = RoomSeekerForm(request.POST)
        if room_seeker_form.is_valid():
            room_seeker = room_seeker_form.save()
        else:
            print(room_seeker_form.errors)
    else:
        room_seeker_form = RoomSeekerForm()

    # Context for the html template
    context_dict = {
        'room_seeker_form':room_seeker_form
    }

    # Render the web page
    response = render(request, "flinder/register_room_seeker.html", context=context_dict)

    return response


def register_room_provider(request):
    # Query the database for any data needed to build the page

    if request.method == 'POST':
        room_provider_form = RoomProviderForm(request.POST)
        if room_provider_form.is_valid():
            room_provider = room_provider_form.save()
        else:
            print(room_provider_form.errors)
    else:
        room_provider_form = RoomProviderForm()

    # Context for the html template
    context_dict = {
        'room_provider_form':room_provider_form
    }

    # Render the web page
    response = render(request, "flinder/register_room_provider.html", context=context_dict)

    return response


def main(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/main.html", context=context_dict)

    return response