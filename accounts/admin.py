from django.contrib import admin
from .models import CustomUser, Profile
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm, UserEditForm


class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserEditForm
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'dob']


