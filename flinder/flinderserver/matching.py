from flinderserver.models import UserProfile, Pictures, InterestsAndPriorities, Swipe;
#More comparisons to be done
from flinderserver.models import UserProfile
import random;
def get_matches(userProfile, n):
    users = UserProfile.objects.all();
    matchedUsers = list();
    while(len(matchedUsers) < n):
        temp = random.choice(users);
        if get_compatability(temp, userProfile) > 0:
            matchedUsers.append(temp);
    return matchedUsers;
    

def get_compatability(user1, user2):
    compatability = 0;
    user1_interests = list();
    user2_interests = list();
    for interest in user1.interests.all():
        user1_interests.append(interest);
    for interest in user2.interests.all():
        user2_interests.append(interest);


    if (not user1.mixedYearOfStudy or not user2.mixedYearOfStudy) and user1.yearOfStudy != user2.yearOfStudy:
        return -10000;
    if (not user1.mixedGender or not user2.mixedGender) and user1.gender != user2.gender:
        return -10000;
    if (not user1.mixedAge or not user2.mixedAge) and user1.yearOfBirth != user2.yearOfBirth:
        return -10000;


    if user1_interests.contains("pets") and user2_interests.contains("pets"):
        compatability += 10;
    else:
        compatability -= 10;
    if user1_interests.contains("food") and user2_interests.contains("food"):
        compatability += 3;
    else:
        compatability -= 3;
    if user1_interests.contains("sports") and user2_interests.contains("sports"):
        compatability += 2;
    else:
        compatability -= 2;
    if user1_interests.contains("music") and user2_interests.contains("music"):
        compatability += 5;
    else:
        compatability -= 5;
    if user1_interests.contains("partying") and user2_interests.contains("partying"):
        compatability += 12;
    else:
        compatability -= 12;
    if user1_interests.contains("drinking") and user2_interests.contains("drinking"):
        compatability += 7;
    else:
        compatability -= 7;
    if user1_interests.contains("flatCleanliness") and user2_interests.contains("flatCleanliness"):
        compatability += 7;
    else:
        compatability -= 7;
    if user1_interests.contains("strictQuietHours") and user2_interests.contains("strictQuietHours"):
        compatability += 15;
    else:
        compatability -= 15;
