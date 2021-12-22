from django.db import models
from django.conf import settings
from datetime import datetime as dt
import datetime
from django.utils import timezone


class Store(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    def get_num_pro(self):
        products = Product.objects.filter(category=self.id)
        return products.count()
    

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'Categorie'

    
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='products', default='no_pic.png', null=True, blank=True)
    price = models.FloatField(help_text='In XAF', default=0.00, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    reorder_quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category', )

    def __str__(self):
        return self.name

    def was_created_recentlyl(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def was_created_this_week(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)

    def was_created_this_month(self):
        return self.created >= timezone.now() - datetime.timedelta(days=30)

class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    purchase_quantity = models.PositiveIntegerField(default=0)
    purchase_created = models.DateTimeField(blank=True)
    purchase_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} purchased by {self.user.username}"

    def was_create_recentlyl(self):
        return self.purchase_created >= timezone.now() - datetime.timedelta(days=1)

    def was_created_this_week(self):
        return self.purchase_created >= timezone.now() - datetime.timedelta(days=7)

    def was_created_this_month(self):
        return self.purchase_created >= timezone.now() - datetime.timedelta(days=30)
    

    def was_created_yesterday(self):
        return self.purchase_created >= timezone.now() - datetime.timedelta(days=1)