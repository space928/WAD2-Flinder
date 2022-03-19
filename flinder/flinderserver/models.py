from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    emailAddress = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    mixedYearOfBirth = models.BooleanField()
    dateOfBirth = models.DateField()
    flatSearcher = models.BooleanField()
    addressLine1 = models.CharField(max_field=128)
    addressLine2 = models.CharField(max_field=128)
    postCode = models.CharField(max_field=7)
    flatBedrooms = models.IntField()
    freeBedrooms = models.IntField()
    university = models.CharField(max_length=30)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other'),
        ('MIX','Mixed') #for flat providers
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
        ('MIX','Mixed'), #for flat providers
    )
    yearOfStudy = models.CharField(max_length=2,choices=YEAR_OF_STUDY_CHOICES)

    class Meta:
    	verbose_name_plural = 'User Profiles'

    def __str__(self):

        return self.name + ", Username: " + self.emailAddress + (" room seeker" if self.flatSearcher else " room provider")

class Pictures(models.Model):
    pictureID = models.AutoField(primary_key=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField()
    description = models.CharField(max_length=256)

    class Meta:
    	verbose_name_plural = 'Pictures'

    def __str__(self):
        return "PictureID: " + self.pictureID + ", posted by " + self.poster


class Preferences(models.Model):
    poster = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    mixedGender = models.BooleanField()
    mixedYearOfStudy = models.BooleanField()
    mixedAge = models.BooleanField()

    class Meta:
    	verbose_name_plural = 'Preferences'

    def __str__(self):
        return "Preferences posted by " + self.poster

class InterestsAndPriorities(models.Model):
    poster = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    pets = models.BooleanField()
    food = models.BooleanField()
    sports = models.BooleanField()
    music = models.BooleanField()
    partying = models.BooleanField()
    drinking = models.BooleanField()
    flatCleanliness = models.BooleanField()
    strictQuietHours = models.BooleanField()

    class Meta:
    	verbose_name_plural = 'Interests and Priorities'

    def __str__(self):
        return "Interests and priorites posted by " + self.poster

class Swipe(models.Model):
    swipeID = models.AutoField(primary_key = True)
    swiper = models.ForeignKey(UserProfile, related_name = 'swiper', on_delete=models.CASCADE)
    swiped = models.ForeignKey(UserProfile, related_name = 'swiped', on_delete=models.CASCADE)
    swipeRight = models.BooleanField()

    class Meta:
    	verbose_name_plural = 'Swipe Actions'

    def __str__(self):
        return self.swiper + " swiped " + self.swiped + ". SwipeID: " + self.swipeID
