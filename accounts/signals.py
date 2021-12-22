from typing import Reversible
from .models import CustomUser, Profile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .utils import random_slug_generator



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# create a slug for the profile
@receiver(pre_save, sender=Profile)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = random_slug_generator(instance)