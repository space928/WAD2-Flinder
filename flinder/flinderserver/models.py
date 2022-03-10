from django.db import models

class User(models.Model):

	userID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	lastName = models.CharField(max_length=128)
	emailAddress = models.EmailField(max_length=128, unique=True)
	dateOfBirth = models.DateField()
	password = models.CharField(widget=forms.PasswordInput)
	flatSearcher = models.BooleanField()

	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other'),
        ('PNTS', 'Prefer not to say'),
    )
	gender = models.CharField(max_length=4,choices=GENDER_CHOICES)

    YEAR_OF_STUDY_CHOICES = (
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
        ('5', '5th Year'),
        ('PGT', 'Postgraduate'),
    )
    yearOfStudy = models.CharField(max_length=2,choices=YEAR_OF_STUDY_CHOICES)

    def __str__(self):
    	return self.name + " " + self.lastName + ", ID: " + self.userID

class Pictures(models.Model):
	pictureID = models.AutoField(primary_key=True)
	poster = models.ForeignKey(User, on_delete=models.CASCADE)
	picture = models.ImageField()
	description = models.CharField(max_length=256)

	def __str__(self):
		return "PictureID: " + self.pictureID + ", posted by " + self.poster


class Preferences(models.Model):
	poster = models.ForeignKey(User, primary_key = True, on_delete=models.CASCADE)
	mixedGender = models.BooleanField()
	mixedYearOfStudy = models.BooleanField()
	mixedAge = models.BooleanField()
	maximumDistance = models.CharField(max_length=10)

	def __str__(self):
		return "Preferences posted by " + self.poster

class InterestsAndPriorities(models.Model):
	poster = models.ForeignKey(User, primary_key = True, on_delete=models.CASCADE)
	pets = models.BooleanField()
	food = models.BooleanField()
	sports = models.BooleanField()
	music = models.BooleanField()
	partying = models.BooleanField()
	drinking = models.BooleanField()
	flatCleanliness = models.BooleanField()
	strictQuietHours = models.BooleanField()

	def __str__(self):
		return "Interests and priorites posted by " + self.poster

class Swipe(models.Model):
	swipeID = models.AutoField(primary_key = True)
	swiper = models.ForeignKey(User, on_delete=models.CASCADE)
	swiped = models.ForeignKey(User, on_delete=models.CASCADE)
	swipeRight = models.BooleanField()

	def __str__(self):
		return self.swiper + " swiped " + self.swiped + ". SwipeID: " + self.swipeID
