from django.shortcuts import render
from flinderserver.models import UserProfile, Pictures, Preferences, InterestsAndPriorities, Swipe


# Create your views here.
def index(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {}

    # Render the web page
    response = render(request, "flinder/index.html", context=context_dict)

    return response


def login(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {}

    model = UserProfile
    fields = ()
    template_name = "flinder/login.html"

    # Render the web page
    response = render(request, template_name, context=context_dict)

    return response


def register(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/register.html", context=context_dict)

    return response


def register_account_type(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/register_account_type.html", context=context_dict)

    return response


def register_room_seeker(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/register_room_seeker.html", context=context_dict)

    return response


def register_room_provider(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

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