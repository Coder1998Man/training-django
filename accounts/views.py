from django.shortcuts import render

from .models import profile

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
