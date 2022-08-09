from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core import paginator
from django.db.models import Q
# Create your views here.

def SearchBar(request):
    query = request.GET.get('q')
    context = {}
    if query:
        users = User.objects.fillter(Q(username__icontains=query))

        paginate = paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator
            }
    return render(request, 'searchbar/search.html', context)