from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('post')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('there was an error logging in, please try again'))
            return redirect('login')
    else:
        return redirect('templates/login.html', {})


