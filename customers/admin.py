from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'is_owing', 'date_created']
    list_filter = ['name', 'phone', 'is_owing']

    prepopulated_fields = {'slug': ('name',)}