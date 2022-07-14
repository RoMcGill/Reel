from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import resolve
from userauthentication.models import Profile
from post.models import Post, Follow


def userProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name
    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted')
    else:
        posts = profile.favourite.all()

    post_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    context = {
        'posts_paginator': posts_paginator,
        'profile': profile,
        'posts': posts,
        'url_name': url_name,
        'following_count': following_count,
        'followers_count': followers_count,
        'post_count': post_count
    }

    return render(request, 'profile.html', context)