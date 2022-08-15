from django.shortcuts import render
from blog.models import BlogPost


# Create your views here.

def BlogPage(request):
    BlogPosts = BlogPost.objects.all()
    return render(request, 'blog-page.html', {'BlogPosts': BlogPosts})