from cProfile import label

from django import forms
from django.db.models import PositiveIntegerField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    phone_number = PositiveIntegerField(null=True)
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
