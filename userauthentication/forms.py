"""
imports
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from userauthentication.models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class editProfileForm(forms.ModelForm):
    """
    class for edit profile form
    """
    picture = forms.ImageField(
        required=True
        )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'First Name'
                 }), required=True),
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input', 'placeholder': 'Last Name'
                }), required=True),
    Location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input', 'placeholder': 'Location'
                }), required=True),
    # url = forms.CharField(
    # widget=forms.TextInput(
    # attrs={
    # 'class': 'input', 'placeholder': 'URL'
    # }), required=True),
    profile_info = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input', 'placeholder': 'profile_info'
                }), required=True)

    class Meta:
        """
        class meta to control fields of form
        """
        model = Profile
        fields = [
            'picture',
            'first_name',
            'last_name',
            'location',
            'url',
            'profile_info'
            ]


class UserRegisterForm(UserCreationForm):
    """
    class for user registration form
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'prompt srch_explore'
                }), max_length=50, required=True
                )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'prompt srch_explore'
                }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',
                'class': 'prompt srch_explore'
                }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class': 'prompt srch_explore'
                }))

    class Meta:
        """
        class meta to control form fields
        """
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
            ]
