from django.urls import path
from userauthentication import views

urlpatterns = [

    path('profile/update', views.editProfile, name='editprofile'),

]