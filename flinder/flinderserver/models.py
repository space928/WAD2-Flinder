from django.db import models

class User(models.Model):

	userID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	lastName = models.CharField(max_length=128)
	emailAddress = models.EmailField(max_length=128, unique=True)
	dateOfBirth = models.DateField()
	password = models.CharField(widget=forms.PasswordInput)
	flatSearcher = models.BooleanField()

	MALE = 'm'
	FEMALE = 'f'
	PREFER_NOT_TO_SAY = 'pnts'
	GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (PREFER_NOT_TO_SAY, 'Prefer not to say'),
    )
	gender = models.CharField(max_length=4,choices=GENDER_CHOICES)

	FIRSTYEAR = '1'
    SECONDYEAR = '2'
    THIRDYEAR = '3'
    FOURTHYEAR = '4'
    FIFTHYEAR = '5'
    POSTGRADUATE = 'pgt'
    YEAR_OF_STUDY_CHOICES = (
        (FIRSTYEAR, '1st Year'),
        (SECONDYEAR, '2nd Year'),
        (THIRDYEAR, '3rd Year'),
        (FOURTHYEAR, '4th Year'),
        (FIFTHYEAR, '5th Year')
        (POSTGRADUATE, 'Postgraduate'),
    )
    yearOfStudy = models.CharField(max_length=2,choices=YEAR_OF_STUDY_CHOICES)

    def __str__(self):
    	return self.userID


class Pictures(models.Model):
	poster = models.ForeignKey(User, on_delete=models.CASCADE)
	picture = models.ImageField()
	description = models.CharField(ax_length=256)

	def __str__(self):
		return self.poster


class Preferences(models.Model):
	poster = models.ForeignKey(User, on_delete=models.CASCADE)
	mixedGender = models.BooleanField()
	mixedYearOfStudy = models.BooleanField()
	moxedAge = models.BooleanField()
	maximumDistance = models.CharField(max_length=10)

	def __str__(self):
		return self.poster

class InterestsAndPriorities(models.Model):
	poster = models.ForeignKey(User, on_delete=models.CASCADE)
	pets = models.BooleanField()
	food = models.BooleanField()
	sports = models.BooleanField()
	music = models.BooleanField()
	partying = models.BooleanField()
	drinking = models.BooleanField()
	flatCleanliness = models.BooleanField()
	strictQuietHours = models.BooleanField()

	def __str__(self):
		return self.poster

class Swipe(models.Model):
	swiper = models.ForeignKey(User, on_delete=models.CASCADE)
	swiped = models.ForeignKey(User, on_delete=models.CASCADE)
	swipeRight = models.BooleanField()

	def __str__(self):
		return self.swiper + " swiped " + self.swiped
