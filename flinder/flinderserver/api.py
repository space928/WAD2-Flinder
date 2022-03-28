# Temp
import json
import ssl
import urllib.request

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
    #gcontext = ssl.SSLContext()  # Dodgy SSL context with no verification
    #r = urllib.request.urlopen("https://api.mockaroo.com/api/7e1549e0?count=10&key=6bc6a940", context=gcontext)
    #result_list = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

    # Set safe to False because we want to return a list of results and not a single object
    #return JsonResponse(result_list, safe=False)
    return JsonResponse([], safe=False)


@login_required
def get_cards(request):
    # Get the user asking for matches
    user = request.user
    #Call the matching algorithm to get the data here
    result_list = flinderserver.matching.get_matches(user,10)
    # Set safe to False because we want to return a list of results and not a single object
    return JsonResponse(result_list, safe=False)


@login_required
def register_swipe(request):
    if request.method == "POST":
        print(request.POST.keys())
        swiper = request.user
        swiped = request.POST["swiped"]
        swipe_direction = request.POST["swipeDir"]

        print(f"Registered swipe from: {swiper} of: {swiped} as: {swipe_direction}")
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})
