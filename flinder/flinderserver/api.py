from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
import flinderserver.matching
from flinderserver.models import Pictures, Swipe
from django.urls import reverse


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


@login_required
def get_matches(request):
    result_list = []
    for swipe in Swipe.objects.filter(swiper=request.user.id, swipeRight=True):
        if (Swipe.objects.filter(swiper=swipe.swiped, swipeRight=True).any()):
            result_list.append({
            "user": swipe.swiped.username.id,
            "photo": Pictures.objects.filter(poster=swipe.swiped.username.id)[0].picture.url,
            "name": swipe.swiped.name,
            "subtitle": f"Flat of {swipe.swiped.flatBedrooms} on {swipe.swiped.addressLine1}",
            "url": reverse('flinder:profile', swipe.swiped.username.id)
        })

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
        swiper = request.user.id
        swiped = request.POST["swiped"]
        swipe_direction = request.POST["swipeDir"] == "true"

        print(f"Registered swipe from: {swiper} of: {swiped} as: {swipe_direction}")
        swipe = Swipe.objects.get_or_create(swiper_id=swiper, swiped_id=swiped)
        swipe.swipeRight = swipe_direction
        swipe.save()

        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})
