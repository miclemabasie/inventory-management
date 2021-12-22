from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to='users', blank=True)
    phone = models.CharField(max_length=15)
    about = models.TextField()
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

