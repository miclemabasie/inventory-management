from django.db.models import fields
from .models import Customer
from django import forms


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'photo', 'phone', 'about']

    