# forms.py

from django import forms

from .models import Comments  # Adjust according to your Comment model location


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']  # Include only the fields you need, e.g., the comment text
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write a comment...', 'rows': 3}),
        }
