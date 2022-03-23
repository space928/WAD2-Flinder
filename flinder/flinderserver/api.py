from django.http import JsonResponse

from flinderserver.models import Swipe, UserProfile, Pictures


# api/get_match?id=1
# result example:
# {
# 	"data": []
# }

def get_match(request):
    # I haven't figure out how to include user in the request
    #user = request.user
    id = request.GET.get('id')
    result = Swipe.objects.filter(swiper_id=id)
    result_list = []
    for title in result:
        current_user = UserProfile.objects.get(username_id=1)
        current_user_picture = Pictures.objects.get(pictureID=title.swiped_id)
        print(current_user)
        member = {"swiped_id": title.swiped_id, "swiper_id": title.swiper_id, "swipeRight": title.swipeRight,
                  "username": current_user.username.email, "photo":current_user_picture.picture.url, "name": current_user.name,
                  "description": current_user_picture.description}
        result_list.append(member)

    return JsonResponse(result_list,safe=False)
