from django.db import models
from products.models import Product
from customers.models import Customer
from accounts.models import CustomUser
from django.utils import timezone
from .utils import generate_code

class Position(models.Model):
    position_id = models.CharField(max_length=12, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.product.price * self.quantity
        if not self.position_id:
            self.position_id = generate_code()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(null=True, blank=True)
    sales_man = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sales for the amount of {self.total_price}"

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created == "":
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()


class DailySale(models.Model):
    transaction_id = models.CharField(max_length=50, blank=True)
    positions = models.ManyToManyField(Position)
    quantity = models.PositiveIntegerField(default=0)
    # total_sale_price = models.FloatField(default=0.0)
    date_created = models.DateTimeField(blank=True)


    def __str__(self):
        return f"{self.transaction_id} - {self.date_created.strftime()}"

class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.filename)