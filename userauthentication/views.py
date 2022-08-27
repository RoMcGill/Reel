"""
imports
"""
from django.shortcuts import HttpResponseRedirect, redirect
from django.shortcuts import render, get_object_or_404
from django.db import transaction
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import resolve, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from userauthentication.models import Profile
from post.models import Post, Follow, Stream
from .forms import editProfileForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@login_required
def UserProfile(request, username):
    """
    function to show user profile
    """
    Profile.objects.get_or_create(
        user=request.user
        )
    user = get_object_or_404(
        User,
        username=username
        )
    profile = Profile.objects.get(
        user=user
        )
    url_name = resolve(
        request.path
        ).url_name
    posts = Post.objects.filter(
        user=user
        ).order_by('-posted')

    if url_name == 'profile':
        posts = Post.objects.filter(
            user=user
            ).order_by('-posted')
    else:
        posts = profile.favourite.all()

    post_count = Post.objects.filter(
        user=user
        ).count()
    following_count = Follow.objects.filter(
        follower=user
        ).count()
    followers_count = Follow.objects.filter(
        following=user
        ).count()

    follow_status = Follow.objects.filter(
        following=user,
        follower=request.user
        ).exists()

    paginator = Paginator(
        posts, 3
        )
    page_number = request.GET.get(
        'page'
        )
    posts_paginator = paginator.get_page(
        page_number
        )

    context = {
        'posts_paginator': posts_paginator,
        'profile': profile,
        'posts': posts,
        'url_name': url_name,
        'following_count': following_count,
        'followers_count': followers_count,
        'post_count': post_count,
        'follow_status': follow_status,
    }

    return render(request, 'profile.html', context)


def follow(request, username, option):
    """
    follow user function
    """
    user = request.user
    following = get_object_or_404(
        User,
        username=username
        )

    try:
        f, created = Follow.objects.get_or_create(
            follower=request.user,
            following=following
            )

        if int(option) == 0:
            f.delete()
            Stream.objects.filter(
                following=following,
                user=request.user
                ).all().delete()
            messages.success(
                request,
                'you have unfollowed another user'
                )
        else:
            posts = Post.objects.all().filter(user=following)[:25]
            with transaction.atomic():
                for post in posts:
                    stream = Stream(
                        post=post,
                        user=request.user,
                        date=post.posted,
                        following=following
                        )
                    stream.save()
        messages.success(
            request,
            'you have followed another user'
            )
        return HttpResponseRedirect(reverse('profile', args=[username]))

    except User.DoesNotExist:
        messages.success(
            request,
            'this user does not exist'
            )
        return HttpResponseRedirect(reverse('profile', args=[username]))


def editProfile(request):
    """
    view to show edit profile form
    """
    user = request.user.id
    profile = Profile.objects.get(
        user__id=user
        )

    if request.method == "POST":
        form = editProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
            )
        if form.is_valid():
            profile.image = form.cleaned_data.get(
                'picture'
                )
            profile.first_name = form.cleaned_data.get(
                'first_name'
                )
            profile.last_name = form.cleaned_data.get(
                'last_name'
                )
            profile.location = form.cleaned_data.get(
                'location'
                )
            profile.profile_info = form.cleaned_data.get(
                'profile_info'
                )
            profile.save()
            messages.success(
                request,
                'you have updated your profile'
                )
            return redirect('profile', profile.user.username)

    else:
        form = editProfileForm(
            instance=request.user.profile
            )
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)
