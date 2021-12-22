from django.urls import path
from .forms import UserLoginForm
from .views import (
    dashboard, 
    register_view, 
    edit_profile,
    profile_view,
    profiles
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    # User athentication and authorization
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(
            authentication_form=UserLoginForm
        ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # others
    path('profile-edit/', edit_profile, name='edit_profile'),
    path('profile-view/<slug:user_slug>/', profile_view, name='profile_view'),
    path('profile-list/', profiles, name='profile_list')
]
