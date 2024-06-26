from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import profile
from .models import CustomUser
from .forms import CustomUserCreationForm, ProfileForm


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'an error occurred during registration!')

    context = {
        'page': page,
        'form': form,
    }

    return render(request, 'accounts/login-register.html', context)


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = CustomUser.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'accounts/login-register.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def profiles(request):
    profiles = profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'accounts/profiles.html', context)


def userProfile(request, pk):
    user_profile = profile.objects.get(id=pk)
    top_skills = user_profile.skill_set.exclude(description__exact="")
    other_skills = user_profile.skill_set.filter(description="")
    context = {
        'user_profile': user_profile,
        'top_skills': top_skills,
        'other_skills': other_skills
    }
    return render(request, 'accounts/user-profile.html', context)

@login_required(login_url=login)
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'accounts/account.html', context)

@login_required(login_url=login)
def edit_account(request):
    form = ProfileForm
    context = {'form': form}
    return render(request, 'accounts/profile-form.html', context)