"""pp4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from userauthentication.views import UserProfile, follow
from members import views as user_views
from searchbar import views as search_views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="reelusers/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="reelusers/logout.html"), name='logout'),
    path('members/', include('members.urls')),
    path('users/', include('userauthentication.urls')),
    path('<username>/', UserProfile, name='profile'),
    path('<username>/svaed/', UserProfile, name='favourite'),
    path('<username>/follow/<option>/', follow, name='follow'),
    path('<username>/showuser/', user_views.showusername, name='showuser'),
    path('searchbar/', include('searchbar.urls')),
    path('<username>/searchbar/', search_views.SearchBar, name='SearchBar'),


]

# django admin customization

admin.site.site_header = "admin for Guess The Boozer"
admin.site.site_title = "guess The Boozer"
admin.site.index_title = "guess The Boozer"


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
