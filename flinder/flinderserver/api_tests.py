from django.test import TestCase
from django.contrib.auth.models import User
from flinderserver.models import UserProfile, Swipe, Pictures
from django.contrib.auth import authenticate, login
from django.test import Client

class TestGetMatches(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='Gianmarco123',email='jlennon@beatles.com',password='password1')
        user2 = User.objects.create_user(username='Luca123',email='rstarr@beatles.com',password='password2')
        user3 = User.objects.create_user(username='Thomas123',email='pmccartney@beatles.com',password='password3')

        UserProfile.objects.create(username=user1,name="Gianmarco", yearOfBirth=2001, flatSearcher=True,
            university="University of Glasgow", mixedGender=True, mixedYearOfStudy=True, mixedAge=True, 
            contactDetails="00436503640361")

        Pictures.objects.create(user1,"flinder/media/images/mountain.png","profile picture")
        
        UserProfile.objects.create(username=user2,name="Luca", yearOfBirth=1999, flatSearcher=True, 
            university="University of Glasgow", mixedGender=True, mixedYearOfStudy=True, mixedAge=True, 
            contactDetails="00436503640361")

        Pictures.objects.create(user2,"flinder/media/images/mountain.png","profile picture")
        
        UserProfile.objects.create(username=user3, name="Thomas", yearOfBirth=1999, flatSearcher=False, addressLine1="Radnor Street 7", addressLine2="2/2", 
            postCode="G37UA", flatBedrooms=4, freeBedrooms=1, university="University of Glasgow", mixedGender=True, mixedYearOfStudy=True, mixedAge=True, 
            contactDetails="00436503640361")

        Pictures.objects.create(user3,"flinder/media/images/mountain.png","profile picture")
        
        Swipe.objects.create(swiper=user1, swiped=user3, swipeRight=True)
        Swipe.objects.create(swiper=user3, swiped=user1, swipeRight=True)

          

    def test_get_matches(self):
        c = Client()
        response = c.post('flinder:login', {'username': 'Gianmarco123', 'password': 'password1'})
        response = c.get('flinder:get_matches')
        response.status_code
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                "user":"pmccartney@beatles.com",
                "photo":"flinder/media/images/mountain.png",
                "name":"Thomas",
                "subtitle":""
            }
        )
        
    
