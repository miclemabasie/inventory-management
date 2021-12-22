from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product
from .utils import random_slug_generator


@receiver(pre_save, sender=Product)
def add_product_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        print('Done with saving the product')
        instance.slug = random_slug_generator(instance)