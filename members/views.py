from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userauthentication.models import Profile


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome To The Guess the boozer Comunity{username}, Edit your Profile')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'reelusers/register.html', {'form': form})


def login(self, request):
    profile = Profile.objects.get(user__id=user)
    if User.is_authenticated:
        messages.success(request, 'you are now logged in!')
        return redirect('edit-profile', profile.user.username)
        
        


@login_required
def showusername(request):
    displaynames = User.objects.all()
    return render(request, 'showuser.html', {"displayusername": displaynames})
