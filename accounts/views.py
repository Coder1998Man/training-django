from django.shortcuts import render

from .models import profile

def profiles(request):
    profiles = profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'accounts/profiles.html', context)