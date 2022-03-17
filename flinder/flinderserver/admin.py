from django.contrib import admin
from flinderserver.models import UserProfile, Pictures, Preferences, InterestsAndPriorities, Swipe

admin.site.register(UserProfile)
admin.site.register(Pictures)
admin.site.register(Preferences)
admin.site.register(InterestsAndPriorities)
admin.site.register(Swipe)
