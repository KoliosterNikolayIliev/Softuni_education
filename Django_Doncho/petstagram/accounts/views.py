from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import SignUpForm, UserProfileForm
from accounts.models import UserProfile
from pets.models import Pet


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    pictures = user.pet_set.all()
    form = UserProfileForm()
    if request.method == 'GET':
        context = {'profile_user': user, 'pets': pictures, 'form': form, }
        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current_user_profile')
        return redirect('current_user_profile')


# yY<RggqxgY]8m7T2
def signup_user(request):
    form = SignUpForm()
    if request.method == 'GET':
        context = {'form': form}

        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user, )
            profile.save()
            login(request, user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
