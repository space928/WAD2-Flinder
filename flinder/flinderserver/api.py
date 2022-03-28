# Temp
import json
import random

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
import flinderserver.matching


# api/get_match?id=1
# result example:
# [
#     {
#         "user":"7ab778e7bc8eb0103",
#         "photo":"media/images/example.png",
#         "name":"Southpark House",
#         "subtitle":"Flat of 3 on Dumbarton Road"
#     },
# ]
from flinderserver.models import Pictures


@login_required
def get_matches(request):
    # Check that this is an API call
    # if request.accepts('text/html'):
    #    return HttpResponseNotAllowed(permitted_methods=["GET"])

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
    with open("./test/flinderCardDataTest.json", "r") as f:
        result_list = random.choices(json.loads(f.read()), k=10)

    # Set safe to False because we want to return a list of results and not a single object
    return JsonResponse(result_list, safe=False)


@login_required
def get_cards(request):
    # Get the user asking for matches
    user = request.user
    # Call the matching algorithm to get the data here
    result_list = []
    for profile in flinderserver.matching.get_matches(user, 10):
        result_list.append({
            "user": profile.username.id,
            "photo": Pictures.objects.filter(poster=profile.username.id)[0].picture.url,
            "name": profile.name,
            "subtitle": f"Flat of {profile.flatBedrooms} on {profile.addressLine1}"
        })

    # Set safe to False because we want to return a list of results and not a single object
    return JsonResponse(result_list, safe=False)


@login_required
def register_swipe(request):
    if request.method == "POST":
        swiper = request.user
        swiped = request.POST["swiped"]
        swipe_direction = request.POST["swipeDir"]

        print(f"Registered swipe from: {swiper} of: {swiped} as: {swipe_direction}")
        
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})
