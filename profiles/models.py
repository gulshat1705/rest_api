from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """ Custom user model """
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    middle_name = models.CharField(max_length=70, null=True, blank=True)
    first_login = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True) #TODO user can select from gallery
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    technology = models.ManyToManyField('Technology', related_name='users')



class Technology(models.Model):
    """ Technology model """
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
