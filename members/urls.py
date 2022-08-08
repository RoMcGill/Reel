
from django.urls import path
from . import views
from members.views import profile


urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('profile/<username>', views.profile, name='profile'),
    
]