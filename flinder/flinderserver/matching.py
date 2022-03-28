from flinderserver.models import UserProfile, Swipe
import random


compatibility_scores = {
    "pets": 10,
    "food": 3,
    "sports": 2,
    "music": 5,
    "partying": 12,
    "drinking": 7,
    "flatCleanliness": 10,
    "strictQuietHours": 15
}


def get_matches(user_profile, n):
    users = UserProfile.objects.all()
    matched_users = []
    while len(matched_users) < n:
        temp = random.choice(users)
        if get_compatability(temp, UserProfile.objects.get(username=user_profile.id)) > 0:
            matched_users.append(temp)
    return matched_users
    

def get_compatability(user1, user2):
    compatability = 0
    user2_interests = set(user2.interests)

    # Don't return matches that don't have compatible yearOfStudy/gender/age preferences
    if (not user1.mixedYearOfStudy or not user2.mixedYearOfStudy) and user1.yearOfStudy != user2.yearOfStudy:
        return -1
    if (not user1.mixedGender or not user2.mixedGender) and user1.gender != user2.gender:
        return -1
    if (not user1.mixedAge or not user2.mixedAge) and user1.yearOfBirth != user2.yearOfBirth:
        return -1

    # Don't return matches that have already been swiped
    if Swipe.objects.filter(swiper=user1.username.id).exists():
        return -1

    for interest in user1.interests:
        if interest in user2_interests:
            compatability += compatibility_scores[interest]
        else:
            compatability -= compatibility_scores[interest]

    return compatability
