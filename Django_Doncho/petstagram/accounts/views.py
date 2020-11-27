

from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import SignUpForm
from accounts.models import UserProfile


def user_profile(request, pk):
    pass

#yY<RggqxgY]8m7T2
def signup_user(request):
    form = SignUpForm()
    if request.method == 'GET':
        context = {'form': form}

        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user,)
            profile.save()
            login(request, user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
