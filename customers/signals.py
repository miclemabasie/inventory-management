from typing import Reversible
from .models import Customer
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .utils import random_slug_generator


# create a slug for the profile
@receiver(pre_save, sender=Customer)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = random_slug_generator(instance)