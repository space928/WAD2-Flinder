from django.contrib.auth.models import User
from django.db import models
import uuid


class InterestsAndPriorities(models.Model):
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
    choice = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = 'Interests and Priorities'

    def __str__(self):
        return self.choice


class UserProfile(models.Model):
    # Fields shared between flat seekers and flat providers are optional
    username = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    yearOfBirth = models.IntegerField()
    flatSearcher = models.BooleanField()
    addressLine1 = models.CharField(max_length=128, null=True, blank=True)
    addressLine2 = models.CharField(max_length=128, null=True, blank=True)
    postCode = models.CharField(max_length=7, null=True, blank=True)
    flatBedrooms = models.IntegerField(null=True, blank=True)
    freeBedrooms = models.IntegerField(null=True, blank=True)
    university = models.CharField(max_length=30)
    BOOL_CHOICES = ((True, 'Mixed'), (False, 'Same'))
    mixedGender = models.BooleanField(choices=BOOL_CHOICES)
    mixedYearOfStudy = models.BooleanField(choices=BOOL_CHOICES)
    mixedAge = models.BooleanField(choices=BOOL_CHOICES)
    contactDetails = models.CharField(max_length=128)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('MIX', 'Mixed'),  # for flat providers
        ('PNTS', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES)

    YEAR_OF_STUDY_CHOICES = (
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
        ('5', '5th Year'),
        ('PGT', 'Postgraduate'),
        ('MIX', 'Mixed'),  # for flat providers
    )
    yearOfStudy = models.CharField(max_length=2, choices=YEAR_OF_STUDY_CHOICES)
    interests = models.ManyToManyField(InterestsAndPriorities)

    class Meta:
        verbose_name_plural = 'User Profiles'
        indexes = [
            models.Index(fields=['username', ]),
            models.Index(fields=['uuid', ]),
        ]

    def __str__(self):
        return self.name + ", Username: " + self.username + (
            " room seeker" if self.flatSearcher else " room provider")


class Pictures(models.Model):
    pictureID = models.AutoField(primary_key=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField()
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return "PictureID: " + self.pictureID + ", posted by " + self.poster


class Swipe(models.Model):
    swipeID = models.AutoField(primary_key=True)
    swiper = models.ForeignKey(User, related_name='swiper', on_delete=models.CASCADE)
    swiped = models.ForeignKey(User, related_name='swiped', on_delete=models.CASCADE)
    swipeRight = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Swipe Actions'

    def __str__(self):
        return self.swiper + " swiped " + self.swiped + ". SwipeID: " + self.swipeID
