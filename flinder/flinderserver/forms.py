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
	birthday = forms.DateField(label="Birthday:")
	yearOfStudy = forms.ChoiceField(label="Year of Study:", choices=UserProfile.YEAR_OF_STUDY_CHOICES)
	gender = forms.ChoiceField(label="Gender:", choices=UserProfile.GENDER_CHOICES)
	university = forms.CharField(label="University:")
	genderPreference = forms.BooleanField(label="Gender Preference:", widget=forms.RadioSelect)
	yearOfStudyPreference = forms.BooleanField(label="Year of Study Preference:", widget=forms.RadioSelect)
	agePreference = forms.BooleanField(label="Age Preference:", widget=forms.RadioSelect)
	interests = forms.MultipleChoiceField(label="Interests:", choices=InterestsAndPriorities.INTERESTS_CHOICES)

	class Meta:
		model = UserProfile
		fields = ('name', 'birthday', 'yearOfStudy', 'gender', 'university',
					'genderPreference', 'yearOfStudyPreference', 'agePreference', 'interests')


#class RoomProviderForm
		


