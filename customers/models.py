from django.db import models
from django.db.models.aggregates import Max
from products.models import Product

class Customer(models.Model):
    # products = models.ManyToManyField(Product, related_name='customer_products', null=True)
    name = models.CharField(max_length=150)
    photo = models.ImageField(null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    about = models.TextField(null=True, blank=True)
    is_owing = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    # def get_all_products_bought(self):
    #     products = Sale.objects.filter(customer=self.id)
    #     return products.count()