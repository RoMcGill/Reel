"""
imports:
"""
from django.urls import path
from . import views


urlpatterns = [

    path('showuser.html/', views.showusername, name='showuser'),

]
