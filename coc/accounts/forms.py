from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import *
from django import forms
# from .models import Community
from django.contrib.auth import authenticate
from django.conf import settings
from .admin import *
from .models import *
from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm, AuthenticationForm
)
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['password', 'new_password1', 'new_password2']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

"""
class ReportForm(forms.Form):
    class Meta:
        model = Report
        fields = ['user', 'content_type', 'content_id', 'content_object', 'reason', 'timestamp']


"""
class JoinCommunityForm(forms.Form):
    community_id = forms.IntegerField(widget=forms.HiddenInput())


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = '__all__'

# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
