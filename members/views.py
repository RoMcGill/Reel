"""
imports
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from userauthentication.models import Profile
from .forms import UserRegisterForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def register(request):
    """
    function to view register form for new user
    """
    if request.method == "POST":
        form = UserRegisterForm(
            request.POST
            )

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get(
                'username'
                )

            messages.success(
                request,
                f'Welcome To The Guess the boozer\
                Comunity{username}, Edit your Profile'
                )

            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'reelusers/register.html',
        {'form': form}
        )


def login(self, request):
    """
    function to view login form for new user
    """
    profile = Profile.objects.get(user__id=user)
    if User.is_authenticated:
        messages.success(
            request,
            'you are now logged in!'
            )
        return redirect(
            'edit-profile',
            profile.user.username
            )



@login_required
def showusername(request):
    """
    function to view username of new user
    """
    displaynames = User.objects.all()
    return render(
        request,
        'showuser.html',
        {"displayusername": displaynames}
        )


from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return render(request,"logout")
    # Redirect to a success page.

# def UserLoggedIn(request):
#     if request.user.is_authenticated == True:
#         username = request.user.username
#     else:
#         username = None
#     return username

# def logout_view(request):
#     username = UserLoggedIn(request)
#     if username != None:
#         logout(request)
#         return redirect('login')

