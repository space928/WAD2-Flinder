from django.test import TestCase
from django.contrib.auth.models import User
from flinderserver.models import UserProfile, Pictures, Swipe

class TestModel(TestCase):

	def setUp(self):
		user = User.objects.create_user(username='Thomas123',email='jlennon@beatles.com',password='glass onion')
		user2 = User.objects.create_user(username='Gianmarco123',email='jlennon21@beatles.com',password='wood onion')

		UserProfile.objects.create(username=user,name="Thomas", yearOfBirth=1999, flatSearcher=True, addressLine1="Radnor Street 7", addressLine2="2/2", 
			postCode="G37UA", flatBedrooms=4, freeBedrooms=2, university="University of Glasgow", mixedGender=True, mixedYearOfStudy=True, mixedAge=True, 
			contactDetails="00436503640361")

		Pictures.objects.create(poster=user,picture="flinder/duck.jpg",description="duck")

		Swipe.objects.create(swiper=user, swiped=user2, swipeRight=True)




	def test_should_create_user(self): 
		userProfile = UserProfile.objects.get(name="Thomas")
		
		user = User.objects.get(username="Thomas123")
		self.assertEqual(userProfile.name, 'Thomas', f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.username,user , f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.yearOfBirth, 1999, f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.addressLine1, "Radnor Street 7", f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.addressLine2, "2/2", f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.postCode, "G37UA", f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.flatBedrooms, 4, f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.freeBedrooms, 2, f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.university, "University of Glasgow", f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.mixedGender, True, f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.mixedYearOfStudy, True, f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.mixedAge, True, f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")
		self.assertEqual(userProfile.contactDetails, "00436503640361", f"Tests on the UserProfile model failed. Check you have all required attributes (including those specified in the exercises!), and try again.")


	def test_should_upload_picture(self):
		picture = Pictures.objects.get(description="duck")
		user = User.objects.get(username="Thomas123")

		self.assertEqual(picture.poster, user, f"Tests on the UserProfile model failed. Check you have all required attribute and try again.")
		self.assertEqual(picture.picture, "flinder/duck.jpg", f"Tests on the UserProfile model failed. Check you have all required attribute and try again.")
		self.assertEqual(picture.description, "duck", f"Tests on the UserProfile model failed. Check you have all required attribute and try again.")


	def test_should_create_swipe(self):
		user = User.objects.get(username="Thomas123")
		user2 = User.objects.get(username="Gianmarco123")

		swipe = Swipe.objects.get(swiper=user)

		self.assertEqual(swipe.swiper, user,f"Tests on the Swipe model failed. Check you have all required attribute and try again.")
		self.assertEqual(swipe.swiped, user2, f"Tests on the Swipe model failed. Check you have all required attribute and try again.")
		self.assertTrue(swipe.swipeRight,f"Tests on the Swipe model failed. Check you have all required attribute and try again.")


