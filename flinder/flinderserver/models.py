from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField
import uuid


class UserProfile(models.Model):
    YEAR_OF_STUDY_CHOICES = (
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
        ('5', '5th Year'),
        ('PGT', 'Postgraduate'),
        ('MIX', 'Mixed'),  # for flat providers
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('MIX', 'Mixed'),  # for flat providers
        ('PNTS', 'Prefer not to say'),
    )
    INTERESTS_CHOICES = (
        ('pets', 'pets'),
        ('food', 'food'),
        ('sports', 'sports'),
        ('music', 'music'),
        ('partying', 'partying'),
        ('drinking', 'drinking'),
        ('flatCleanliness', 'flatCleanliness'),
        ('strictQuietHours', 'strictQuietHours')
    )
    BOOL_CHOICES = ((True, 'Mixed'), (False, 'Same'))

    # Fields shared between flat seekers and flat providers are optional
    username = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES)
    yearOfBirth = models.IntegerField()
    yearOfStudy = models.CharField(max_length=2, choices=YEAR_OF_STUDY_CHOICES)
    university = models.CharField(max_length=30)
    interests = MultiSelectField(choices=INTERESTS_CHOICES)
    contactDetails = models.CharField(max_length=128)

    flatSearcher = models.BooleanField()

    addressLine1 = models.CharField(max_length=128, null=True, blank=True)
    addressLine2 = models.CharField(max_length=128, null=True, blank=True)
    postCode = models.CharField(max_length=7, null=True, blank=True)
    flatBedrooms = models.IntegerField(null=True, blank=True)
    freeBedrooms = models.IntegerField(null=True, blank=True)

    mixedGender = models.BooleanField(choices=BOOL_CHOICES)
    mixedYearOfStudy = models.BooleanField(choices=BOOL_CHOICES)
    mixedAge = models.BooleanField(choices=BOOL_CHOICES)

    class Meta:
        verbose_name_plural = 'User Profiles'
        indexes = [
            models.Index(fields=['username', ]),
            models.Index(fields=['uuid', ]),
        ]

    def __str__(self):
        return f"{self.name}, Username: {self.username.username}, room {('seeker' if self.flatSearcher else 'provider')}"


class Pictures(models.Model):
    pictureID = models.AutoField(primary_key=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return f"PictureID: {self.pictureID}, posted by {self.poster}"


class Swipe(models.Model):
    swipeID = models.AutoField(primary_key=True)
    swiper = models.ForeignKey(User, related_name='swiper', on_delete=models.CASCADE)
    swiped = models.ForeignKey(User, related_name='swiped', on_delete=models.CASCADE)
    swipeRight = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Swipe Actions'

    def __str__(self):
        return f"{self.swiper} swiped {self.swiped}. SwipeID: {self.swipeID}"
