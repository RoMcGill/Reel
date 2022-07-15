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
from userauthentication.models import Profile
from userauthentication.views import userProfile, follow, editProfile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('users/', include('userauthentication.urls')),
    path('<username>/', userProfile, name='profile'),
    path('<username>/svaed/', userProfile, name='favourite'),
    path('<username>/follow/<option>/', follow, name='follow'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

