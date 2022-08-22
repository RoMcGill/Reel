"""
    Imports
"""
from django.shortcuts import render
from blog.models import blogpost


# Create your views here.

def blog_page(request):
    """
    A function to show the blog post model
    """
    blog_posts = blogpost.objects.all()
    return render(request, 'blog-page.html', {'blog_posts': blog_posts})
