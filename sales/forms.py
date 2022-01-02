from django import forms
from .models import Sale, Position, CSV


class AddPositionForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    customer_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control ', 'placeholder': 'customer', 'id': 'customer_id'}), required=False)

    class Meta:
        model = Position
        fields = ('position_id', 'customer_name', 'product', 'quantity', 'price', 'date')

        widgets = {
            'position_id': forms.HiddenInput()
        }


class SaleConfirmForm(forms.Form):
    name = forms.CharField(required=False)
    
