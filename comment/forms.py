"""
    Imports
"""
from django import forms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from comment.models import Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CommentForm(forms.ModelForm):
    """
    A form for the comment model
    """

    body = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input', 'placeholder': 'Comment'}
            ), required=True
        )

    class Meta:
        """
        A meta for the comment body
        """
        model = Comment
        fields = ['body']
