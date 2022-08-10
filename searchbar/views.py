from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def SearchBar(request):
    query = request.GET.get('q')
    context = {}
    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Paginator
        paginator = Paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
            }

    return render(request, 'search.html', context)