from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import CustomUser, Profile
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm


# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


@login_required
def dashboard(request):
    user = request.user
    template_name = 'dashboard.html'
    context = {
        'user': user,
        'page_name': 'Dashboard',
        'section': 'dashboard'
    }
    return render(request, template_name, context)


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password1')
        user = form.save(commit=False)
        # set the current user password
        user.set_password(password)
        user.save()
        
        template_name = 'registration/register_done.html'
        context = {
            'user': user
        }
        return render(request, template_name, context)
    template_name = 'registration/register.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user_edit_form = UserEditForm(instance=user, data=request.POST)
        profile_edit_form = ProfileEditForm(
            instance=user.profile,
            data = request.POST,
            files = request.FILES
        )
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save(commit=False)
            user_edit_form.user = user
            user_edit_form.save()
            profile_edit_form.save()

            messages.success(request, 'You have successfully updated your profile!')
            return redirect()
        else:
            messages.error(request, 'Opps!! something went wrong.')
            print(profile_edit_form.errors())
            print(user_edit_form.errors())
    else:
        user_edit_form = UserEditForm(instance=user)
        profile_edit_form = ProfileEditForm(instance=user.profile)
    template_name = 'profiles/edit.html'
    context = {
        'user': user,
        'user_form': user_edit_form,
        'profile_form': profile_edit_form
    }
    return render(request, template_name, context)

@login_required
def profile_view(request, user_slug):
    profile = get_object_or_404(Profile, slug=user_slug)

    template_name = 'profiles/profile_detail.html'

    context = {
        'profile': profile,
    }
    return render(request, template_name, context)

@login_required
def profiles(request):
    profiles = Profile.objects.filter(user__is_active=True)
    template_name = 'profiles/profile_list.html'
    context = {
        'profiles': profiles
    }

    return render(request, template_name, context)