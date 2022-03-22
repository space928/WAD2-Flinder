from django.http import JsonResponse

from flinderserver.models import Swipe


# api/get_match?id=1
# result example:
# {
# 	"status": "0",
# 	"msg": "",
# 	"data": []
# }

def get_match(request):
    id = request.GET.get('id')
    result = Swipe.objects.filter(swiper_id=id)
    result_list = []
    for title in result:
        member = {"swiped_id": title.swiped_id, "swiper_id": title.swiper_id, "swipeRight": title.swipeRight}
        result_list.append(member)

    return JsonResponse({"status": "0", "msg": "", "data": result_list})
