from django.urls import path
from searchbar import views


urlpatterns = [

    path('new/', views.SearchBar, name='SearchBar'),
    
]