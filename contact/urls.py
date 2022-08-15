from django.urls import path,include
from . import views

urlpatterns = [
    path('contact_us/',views.contact_us,name='contact_us')
]