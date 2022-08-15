from django.contrib.auth.models import User
from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):

    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Comment'}), required=True)
    
    

    class Meta:
        model = Comment
        fields = ['body']
    