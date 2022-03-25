from django.contrib import admin
from flinderserver.models import UserProfile, Pictures, InterestsAndPriorities, Swipe

admin.site.register(UserProfile)
admin.site.register(Pictures)
admin.site.register(InterestsAndPriorities)
admin.site.register(Swipe)
