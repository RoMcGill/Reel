from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome To The Reel Comunity {username}! Now Login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'reelusers/register.html', {'form':form})

@login_required
def login(self, request):
    if User.is_authenticated:
        return HttpResponseRedirect(reverse('profile', args=[username]))