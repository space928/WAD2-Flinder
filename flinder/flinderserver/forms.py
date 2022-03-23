from django import forms
from flinderserver.models import UserProfile, InterestsAndPriorities
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username = forms.CharField(label="Username:", required=False)
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','password')

class RoomSeekerForm(forms.ModelForm):
	name = forms.CharField(label="Name:")
	yearOfBirth = forms.IntegerField(label="Year of birth")
	yearOfStudy = forms.ChoiceField(label="Year of study:", choices=UserProfile.YEAR_OF_STUDY_CHOICES)
	gender = forms.ChoiceField(label="Gender:", choices=UserProfile.GENDER_CHOICES)
	university = forms.CharField(label="University:")
	genderPreference = forms.ChoiceField(label="Gender preference:", widget=forms.RadioSelect, choices=UserProfile.BOOL_CHOICES)
	yearOfStudyPreference = forms.ChoiceField(label="Year of study preference:", widget=forms.RadioSelect, choices=UserProfile.BOOL_CHOICES)
	agePreference = forms.ChoiceField(label="Age preference:", widget=forms.RadioSelect, choices=UserProfile.BOOL_CHOICES)
	interests = forms.MultipleChoiceField(label="Interests:", choices=InterestsAndPriorities.INTERESTS_CHOICES)

	class Meta:
		model = UserProfile
		fields = ('name', 'yearOfBirth', 'yearOfStudy', 'gender', 'university',
					'genderPreference', 'yearOfStudyPreference', 'agePreference', 'interests')


class RoomProviderForm(forms.ModelForm):
	name = forms.CharField(label="Group name:")
	yearOfBirth = forms.IntegerField(label="Year of birth:")
	yearOfStudy = forms.ChoiceField(label="Year of study:", choices=UserProfile.YEAR_OF_STUDY_CHOICES)
	gender = forms.ChoiceField(label="Gender:", choices=UserProfile.GENDER_CHOICES)
	university = forms.CharField(label="University:")
	addressLine1 = forms.CharField(label="Address line 1:")
	addressLine2 = forms.CharField(label="Address line 2:")
	postCode = forms.CharField(label="Post code:")
	numberOfBedrooms = forms.IntegerField(label="Number of bedrooms:")
	availableBedrooms = forms.IntegerField(label="Bedrooms available:")

	class Meta:
		model = UserProfile
		fields = ('name', 'yearOfBirth', 'yearOfStudy', 'gender', 'university',
					'addressLine1', 'addressLine2', 'postCode', 'numberOfBedrooms','availableBedrooms')





		


