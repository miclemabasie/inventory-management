from django import forms
from django.db.models import fields
from .models import CustomUser
from django.forms.widgets import PasswordInput
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # check if username exist in the database
        qs = CustomUser.objects.filter(username__iexact=username)

        if len(qs) < 1:
            raise forms.ValidationError('No user found with this name in the database')
        return username


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        # check if username is already taken inthe database
        qs = CustomUser.objects.filter(username__iexact=username)
        if qs:
            raise forms.ValidationError('This username is already taken, please chose another')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('This passwords do not match')
        else:
            return password2

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']

    
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'about', 'dob']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control ', 'placeholder': 'Username', 'id': 'id_username'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'id_password',
            }
    ))
    



# <tr><th><label for="id_username">Username:</label></th><td><input type="text" name="username" autofocus autocapitalize="none" autocomplete="username" maxlength="150" required id="id_username"></td></tr>
# <tr><th><label for="id_password">Password:</label></th><td><input type="password" name="password" autocomplete="current-password" required id="id_password"></td></tr>