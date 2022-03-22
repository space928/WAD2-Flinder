from django.http import JsonResponse

from flinderserver.models import Swipe


def get_match(request):
    id = request.GET.get('id')
    print(id)
    result = Swipe.objects.filter(swiper_id=id)
    result_list = []
    for title in result:
        member = {}
        member["swiped_id"] = title.swiped_id
        member["swiper_id"] = title.swiper_id
        member["swipeRight"] = title.swipeRight
        result_list.append(member)

    return JsonResponse({"status": "0", "msg": "", "data": result_list})
