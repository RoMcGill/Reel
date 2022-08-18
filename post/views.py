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
# from userauthentication.models import Profile
# from notify.utilities import create_notification
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def index(request):
    """
    view for index page
    """
    user = request.user
    posts = Stream.objects.filter(user=user)
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
            # ### notifications (bug) ######
            # create_notification(request, comment.body,/
            #  'comment.first_name', extra_id=0)
            # ### notifications (bug) ######
        return HttpResponseRedirect(reverse("post-detail", args=[post_id]))
    else:
        form = CommentForm()

    context = {
        'form': form,
        'comments': comments,
        'post': post,
    }
    return render(request, 'post-detail.html', context)

# ##################################################################
# ###################### delete comment ############################
# ##################################################################

# def comment_delete_view(request, id=None):

#     comment= get_object_or_404(Comment, id=id)

#     creator= comment.user.username

#     if request.method == "POST" and request.user.is_authenticated \
# and request.user.username == creator:
#         comment.delete()
#         messages.success(request, "Post successfully deleted!")
#         return HttpResponseRedirect(reverse("post-detail", args=[post_id]))

#     context= {'content': content,
#               'creator': creator,
#               }

#     return render(request, 'post-detail.html', context)


# ##################################################################
# ###################### delete comment ############################
# ##################################################################


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
    else:
        profile.favourite.add(
            post
            )
    return HttpResponseRedirect(reverse('post-detail', args=[post_id]))

# ##################################################################
# ###################### solved button ############################
# ##################################################################
# def solve(request, post_id):
#     """
#     view to show likes
#     """
#     user = request.user
#     post = Post.objects.get(id=post_id)
#     current_solves = post.solves
#     solved = Solves.objects.filter(
#         user=user,
#         post=post
#         ).count()

#     if not solved:
#         Solves.objects.create(
#             user=user,
#             post=post
#             )
#         current_solves = current_solves + 1
#         messages.success(
#             request,
#             'your post has been solved'
#             )

#     else:
#         Solves.objects.filter(
#             user=user,
#             post=post
#             ).delete()
#         current_solves = current_solves - 1
#         messages.success(request, 'your post is not solved')

#     post.solves = current_solves
#     post.save()
#     return HttpResponseRedirect(reverse('post-detail', args=[post_id]))

# ##################################################################
# ###################### solved button ############################
# ##################################################################
