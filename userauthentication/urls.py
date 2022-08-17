"""
imports
"""
from django.urls import path
from userauthentication.views import UserProfile, editProfile
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('profile/update', views.editProfile, name='editProfile'),
    # path('sign-in/', views.register, name='sign-in'),
    # path('sign-up/', auth_views.LoginView.as_view(template_name='sign-in.html', redirect_authenticated_user=True), name='sign-in'),
    # path('sign-out/', auth_views.LogoutView.as_view(template_name='sign-out.html'), name='sign-out'),

]