"""
    Imports
"""
from django.shortcuts import render
from blog.models import BlogPost


# Create your views here.

def blog_page(request):
    """
    A function to show the blog post model
    """
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog-page.html', {'blog_posts': blog_posts})
