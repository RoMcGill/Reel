"""
imports
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from post.models import Tag, Stream, Post, Likes
from post.forms import NewPostForm
from userauthentication.models import Profile
from comment.models import Comment
from comment.forms import CommentForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def index(request):
    """
    view for index page
    """
    user = request.user
    posts = Stream.objects.all().order_by('-date')
    group_ids = []
    for post in posts:
        group_ids.append(post.post_id)
    post_items = Post.objects.filter(
        id__in=group_ids).all().order_by('-posted')
    context = {
        'post_items': post_items
    }
    return render(request, 'index.html', context)


def NewPost(request):
    """
    view for creating new post
    """
    user = request.user.id
    tags_objs = []
    profile = Profile.objects.get(user__id=user)

    if request.method == "POST":
        form = NewPostForm(
            request.POST,
            request.FILES
            )
        if form.is_valid():
            picture = form.cleaned_data.get(
                'picture'
                )
            caption = form.cleaned_data.get(
                'caption'
                )
            tag_form = form.cleaned_data.get(
                'tag'
                )
            tags_list = list(
                tag_form.split(',')
                )

            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)
            p, created = Post.objects.get_or_create(
                picture=picture,
                caption=caption,
                user_id=user
                )
            p.tag.set(
                tags_objs
                )
            p.save()
            messages.success(
                request,
                'you created a Post')
            return redirect(
                'profile',
                profile.user.username)
    else:
        form = NewPostForm()
    context = {
        'form': form
    }
    return render(request, 'newpost.html', context)


def PostDetail(request, post_id):
    """
    view to show post detail page
    """
    post = get_object_or_404(
        Post,
        id=post_id
        )

    # comment
    comments = Comment.objects.filter(post=post).order_by("-date")

    # commentForm
    if request.method == "POST":
        form = CommentForm(
            request.POST,
            request.FILES
            )
        if form.is_valid():
            comment = form.save(
                commit=False
                )
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(
                request,
                'you have commented on a users post'
                )
        return HttpResponseRedirect(reverse("post-detail", args=[post_id]))
    else:
        form = CommentForm()

    context = {
        'form': form,
        'comments': comments,
        'post': post,
    }
    return render(request, 'post-detail.html', context)


def delete_comment(request, comment_id):
    """
    Deletes a comment for the user
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Your comment has been deleted')
    return redirect(request.META.get('HTTP_REFERER', '/'))


def tags(request, tag_slug):
    """
    view to show tags
    """
    tag = get_object_or_404(
        Tag,
        slug=tag_slug
        )
    posts = Post.objects.filter(tag=tag).order_by('-posted')

    context = {
        'posts': posts,
        'tag': tag
    }
    return render(request, 'tags.html', context)


def like(request, post_id):
    """
    view to show likes
    """
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(
        user=user,
        post=post
        ).count()

    if not liked:
        Likes.objects.create(
            user=user,
            post=post
            )
        current_likes = current_likes + 1
        messages.success(
            request,
            'you liked a Post'
            )

    else:
        Likes.objects.filter(
            user=user,
            post=post
            ).delete()
        current_likes = current_likes - 1
        messages.success(request, 'you unliked a Post')

    post.likes = current_likes
    post.save()
    return HttpResponseRedirect(reverse('post-detail', args=[post_id]))


def favourite(request, post_id):
    """
    view to show favourit posts
    """
    user = request.user
    post = Post.objects.get(
        id=post_id
        )
    profile = Profile.objects.get(
        user=user
        )
    if profile.favourite.filter(id=post_id).exists():
        profile.favourite.remove(
            post
            )
        messages.success(
            request,
            'Post removed from favourites'
            )
    else:
        profile.favourite.add(
            post
            )
        messages.success(
            request,
            'Post added to favourites'
            )
    return HttpResponseRedirect(reverse('post-detail', args=[post_id]))
