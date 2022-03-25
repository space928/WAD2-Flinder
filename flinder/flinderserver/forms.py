from django import forms
from flinderserver.models import UserProfile
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class UserForm(forms.ModelForm):
    username = forms.CharField(label="Username:", required=False)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

        
class RoomSeekerForm(forms.ModelForm):
    name = forms.CharField(label="Name:")
    YEAR_OF_BIRTH_CHOICES = tuple([(i, str(i)) for i in range(1950, 2050)])
    yearOfBirth = forms.ChoiceField(label="Year of birth:", choices=YEAR_OF_BIRTH_CHOICES)
    yearOfStudy = forms.ChoiceField(label="Year of study:", choices=UserProfile.YEAR_OF_STUDY_CHOICES)
    gender = forms.ChoiceField(label="Gender:", choices=UserProfile.GENDER_CHOICES)
    university = forms.CharField(label="University:")
    contactDetails = forms.CharField(label='Contact details:', widget=forms.Textarea)

    mixedGender = forms.ChoiceField(label="Gender preference:", widget=forms.RadioSelect,
                                    choices=UserProfile.BOOL_CHOICES)
    mixedYearOfStudy = forms.ChoiceField(label="Year of study preference:", widget=forms.RadioSelect,
                                         choices=UserProfile.BOOL_CHOICES)
    mixedAge = forms.ChoiceField(label="Age preference:", widget=forms.RadioSelect,
                                 choices=UserProfile.BOOL_CHOICES)
    interests = forms.MultipleChoiceField(label="Interests:", choices=UserProfile.INTERESTS_CHOICES)

    class Meta:
        model = UserProfile
        fields = ('name', 'yearOfBirth', 'yearOfStudy', 'gender', 'university',
                  'mixedGender', 'mixedYearOfStudy', 'mixedAge', 'interests')

    
class RoomProviderForm(forms.ModelForm):
    name = forms.CharField(label="Group name:")
    YEAR_OF_BIRTH_CHOICES = tuple([(-1, "Mixed")] + [(i, str(i)) for i in range(1950, 2050)])
    yearOfBirth = forms.ChoiceField(label="Year of birth:", choices=YEAR_OF_BIRTH_CHOICES)
    yearOfStudy = forms.ChoiceField(label="Year of study:", choices=UserProfile.YEAR_OF_STUDY_CHOICES)
    gender = forms.ChoiceField(label="Gender:", choices=UserProfile.GENDER_CHOICES)
    university = forms.CharField(label="University:")
    contactDetails = forms.CharField(label='Contact details:')

    addressLine1 = forms.CharField(label="Address line 1:")
    addressLine2 = forms.CharField(label="Address line 2:", required=False)
    postCode = forms.CharField(label="Post code:")
    numberOfBedrooms = forms.IntegerField(label="Number of bedrooms:", validators=[MinValueValidator(1)])
    availableBedrooms = forms.IntegerField(label="Bedrooms available:", validators=[MinValueValidator(1)])

    mixedGender = forms.ChoiceField(label="Gender preference:", widget=forms.RadioSelect,
                                    choices=UserProfile.BOOL_CHOICES)
    mixedYearOfStudy = forms.ChoiceField(label="Year of study preference:", widget=forms.RadioSelect,
                                         choices=UserProfile.BOOL_CHOICES)
    mixedAge = forms.ChoiceField(label="Age preference:", widget=forms.RadioSelect,
                                 choices=UserProfile.BOOL_CHOICES)
    interests = forms.MultipleChoiceField(label="Interests:", choices=UserProfile.INTERESTS_CHOICES)

    class Meta:
        model = UserProfile
        fields = ('name', 'yearOfBirth', 'yearOfStudy', 'gender', 'university',
                  'addressLine1', 'addressLine2', 'postCode', 'numberOfBedrooms', 'availableBedrooms',
                  'mixedGender', 'mixedYearOfStudy', 'mixedAge', 'interests')
