from django.urls import path,include
from . import views

urlpatterns = [
    path('blog/',views.BlogPage, name='blog')
]