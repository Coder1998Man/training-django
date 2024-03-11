from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import profile
from .models import CustomUser


def login_user(request):

    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username or password is incorrect')

    return render(request, 'accounts/login-register.html')


def logout_user(request):
    logout(request)
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
