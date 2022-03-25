from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed

from flinderserver.models import Swipe, UserProfile, Pictures

# Temp
import urllib.request
import json


# api/get_match?id=1
# result example:
# [
#     {
#         "user":"hello@example.com",
#         "photo":"media/images/example.png",
#         "name":"Southpark House",
#         "subtitle":"Flat of 3 on Dumbarton Road"
#     },
# ]

@login_required
def get_matches(request):
    # Check that this is an API call
    if request.accepts('text/html'):
        return HttpResponseNotAllowed(permitted_methods=["GET"])

    """ TODO: Uncomment, once backend is complete
    result = Swipe.objects.filter(swiper_id=request.user.username)
    result_list = []
    for title in result:
        current_user = UserProfile.objects.get(username_id=1)
        current_user_picture = Pictures.objects.get(pictureID=title.swiped_id)[0]
        print(current_user)
        member = {"swiped_id": title.swiped_id, "swiper_id": title.swiper_id, "swipeRight": title.swipeRight,
                  "username": current_user.username.email, "photo": current_user_picture.picture.url,
                  "name": current_user.name,
                  "description": current_user_picture.description}
        result_list.append(member)"""

    # TODO: Remove once backend work is complete
    result_list = json.loads(urllib.request.urlopen("https://api.mockaroo.com/api/7e1549e0?count=10&key=6bc6a940"))

    return JsonResponse(result_list, safe=False)


@login_required
def get_cards(request):
    # Check that this is an API call
    if request.accepts('text/html'):
        return HttpResponseNotAllowed(permitted_methods=["GET"])

    # Get the user asking for matches
    user = request.user
    # TODO: Call the matching algorithm to get the data here
    matches = json.loads(urllib.request.urlopen("https://api.mockaroo.com/api/7e1549e0?count=10&key=6bc6a940"))

    return JsonResponse(matches)
