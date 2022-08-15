from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse
from django.contrib import messages

def contact_us(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'Thank You for getting in touch with us!')
        return redirect('index')
        

    return render(request, 'contact_us.html')

# Create your views here.
