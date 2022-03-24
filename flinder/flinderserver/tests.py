from django.test import TestCase
from django.contrib.auth.models import User
from flinderserver.models import UserProfile

class TestModel(TestCase):

	def setUp(self):
		user = User.objects.create_user(username='Thomas123',email='jlennon@beatles.com',password='glass onion')

		UserProfile.objects.create(username=user,name="Thomas", yearOfBirth=1999, flatSearcher=True, addressLine1="Radnor Street 7", addressLine2="2/2", 
			postCode="G37UA", flatBedrooms=4, freeBedrooms=2, university="University of Glasgow", mixedGender=True, mixedYearOfStudy=True, mixedAge=True, 
			contactDetails="00436503640361")

		
	    

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
		
      