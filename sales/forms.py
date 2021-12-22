from django import forms
from .models import Sale, Position, CSV


class AddPositionForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Position
        fields = ('position_id', 'product', 'quantity', 'price', 'date')

        widgets = {
            'position_id': forms.HiddenInput()
        }


class SaleConfirmForm(forms.Form):
    name = forms.CharField(required=False)
    
