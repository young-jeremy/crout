from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import *
from allauth.socialaccount.models import SocialAccount
from notifications.models import Notifications
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import user_passes_test
from django import views
from django.views.generic import ListView
from .admin import *
from django.http import JsonResponse
import stripe
from videos.models import *
from google.cloud import vision
# from rest_framework import status, generics
from .admin import *
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, logout
from .forms import *
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import requests
from django.template.loader import render_to_string
import django.utils.encoding
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.http import Http404
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from .models import *
from django.apps import apps
from django_cleanup import cleanup
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import serializers
from .admin import *

apps.get_models()
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from .forms import CustomPasswordChangeForm
from notifications.models import *
from django.contrib.auth.views import PasswordResetCompleteView
from django.shortcuts import redirect
from notifications.utils import send_email_notification
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from allauth.account.signals import password_changed
from django.dispatch import receiver
from notifications.utils import send_email_notification


@receiver(password_changed)
def notify_password_changed(request, user, **kwargs):
    send_email_notification(
        user,
        subject="Password Reset Successful",
        message="Your password has been reset successfully. If this was not you, please contact support immediately."
    )


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)

        # Send notification
        user_email = self.request.session.get('reset_user_email')  # Store email in session during reset
        if user_email:
            try:
                user = User.objects.get(email=user_email)
                send_email_notification(
                    user,
                    subject="Password Reset Successful",
                    message="Your password has been reset successfully. If this was not you, please contact support immediately."
                )
            except User.DoesNotExist:
                pass  # Handle invalid user email

        return response


def custom_password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # Handle password reset form submission and saving here
        # After saving the new password:
        send_email_notification(
            user,
            subject="Password Reset Successful",
            message="Your password has been reset successfully. If this was not you, please contact support immediately."
        )
        return redirect('password_reset_complete')
    else:
        return HttpResponse("Password reset link is invalid or expired.")


def accounts_settings_and_privacy(request):
    template_name = 'accounts/account_settings_and_privacy.html'
    return render(request, template_name)


def account_settings(request):
    template_name='accounts/settings.html'
    return render(request, template_name)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Save the new password
            form.save()

            # Update session to keep the user logged in after password change
            update_session_auth_hash(request, form.user)

            # Get the user's notification settings
            notification_settings = request.user.notification_settings

            # If the user wants to be notified about password changes
            if notification_settings.should_notify('password_change'):
                # Send email about password change
                send_mail(
                    'Password Changed',
                    'Your password has been successfully changed.',
                    'jeremymayaka96@gmail.com',  # Sender email
                    [request.user.email],  # Recipient email
                )

            return redirect('accounts:password_change_done')  # Redirect to a success page
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'accounts/profile.html', {'form': form})


# views.py (continued)

def password_change_done(request):
    return render(request, 'accounts/password_change_done.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That username is taken')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'That email is being used')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(username=username, password=password, email=email,
                                                        first_name=first_name, last_name=last_name)

                        user.save()
                        messages.success(request, 'You are now registered and can log in')
                        return redirect('login')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('register')
        else:
            form = UserCreationForm()
    return render(request, 'accounts/register.html')


def apps(request):
    template_name = 'accounts/apps.html'
    return render(request, template_name)


@login_required()
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile_form = form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm
    return render(request, 'accounts/create_users.html', {'form': form})


def update_profile(request):
    template_name = 'accounts/update_profile.html'
    user_profile = UserProfile.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ProfileForm()
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        else:
            form = ProfileForm(instance=user_profile)
        return render(request, template_name, {'form': form})


def post_comment(request):
    if request.session.get('has_commented', False):
        return HttpResponse('you have already commented!')
    # c = comments.Comment(comment=new_comment)
    # c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for commenting')


def password_reset_request(request):
    template_name = 'accounts/password_reset.html'
    if request.method == 'POST':
        domain = request.headers['Host']
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = 'Password Request Reset'
                    email_template_name = 'accounts/password_reset_email.txt'
                    c = {
                        'email': user.email,
                        'domain': 'domain',
                        'site_name': 'Interface',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'protocol': 'http',
                        'user': user,
                        'token': default_token_generator.make_token(user),
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse("Invalid Header found")
                    return redirect('accounts/password_reset/done/')
    password_reset_form = PasswordResetForm()
    context = {
        'password_reset_form': password_reset_form,
    }
    return render(request, template_name, context)


def mark_all_as_read(request):
    template_name = 'users/notifications.html'
    Notifications.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return redirect('notifications:notifications')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:login')
        else:
            messages.info(request, 'Please correct the errors before proceeding')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'accounts/register.html', {'form': form})


def email_check(user):
    return user.email.endswith('@example.com')


def login_view(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_form = authenticate(username=username, password=password)
            if user_form is not None:
                login(request, user_form)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('videos:home')
            else:
                if not request.user.email.endswith('@example.com'):
                    return redirect('/login/?next=%s' % request.path)
                else:
                    messages.error(request, "Invalid username or password.")
                    request.session.set_test_cookie()
        else:
            messages.error(request, "Invalid username or password.")

    else:
        messages.info(request, 'There is something wrong, check if there is a problem before logging in again')
        form = AuthenticationForm()
    return render(request=request, template_name="accounts/login.html",
                  context={"form": form, })


def sign_up(request):
    template_name = 'accounts/sign_up.html'
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('posts')
        else:
            return render(request, template_name, {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user_form = authenticate(username=username, password=raw_password)
            login(request, user_form, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home:home')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'accounts/register.html', {'form': form})


@login_required(login_url='accounts/login')
def logout_view(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    logout(request)
    return redirect('videos:home')


@login_required(login_url='accounts/login')
def profile(request):
    my_user_profile = UserProfile.objects.filter(email=request.user.profile).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile Was Updated Successfully!')
            return redirect('accounts:update_profile')
        messages.info(request, 'Click On  Edit Profile To Make Important Changes To Your Profile To Help Us track You')
        return render(request, 'accountsaccountsaccounts/profile.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        return render(request, 'accounts/profile.html', {'form': form, 'my_user_profile': my_user_profile})


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            form = PasswordChangeForm(user=request.user)
            return render(request, 'accounts/password_reset.html', {'form': form})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/password_reset.html', {'form': form})


def process_payment(user, amount):
    try:
        charge = stripe.Charge.create(
            amount=int(amount * 100),
            currency='usd',
            source=user.payment_source,
        )
    except stripe.error.StripeError as e:
        print('There are error, kindly check before trying out')


def distribute_revenue(video, revenue):
    creators = video.creators.all()
    for creator in creators:
        share = (creator.revenue_sharing_rule.percentage_share / 100) * revenue
        # Transfer share to the content creator's account
        # Example: creator.account_balance += share
        creator.save()


def check_for_nudity(image_url):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_url

    response = client.safe_search_detection(image=image)
    safe_search = response.safe_search_annotation

    return safe_search.adult == vision.Likelihood.LIKELY or safe_search.violence == vision.Likelihood.LIKELY


def create_user_profile(request):
    if not hasattr(request.user, 'userprofile'):
        user_profile = UserProfile(user=request.user)
        user_profile.save()
        return redirect('accounts:profile_edit')


def create_community(request):
    template_name = 'accounts/create_community.html'
    form = CommunityForm()
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('accounts:community_list')
        else:
            form = CommunityForm()
    return render(request, template_name, {'form': form})


def community_list(request):
    template_name = 'accounts/community_list.html'
    view_communities = Community.objects.all()

    return render(request, template_name, {'view_communities': view_communities})


def community_details(request, community_id):
    template_name = 'accounts/community_details.html'
    community = Community.objects.get(id=community_id)
    return render(request, template_name, {'community': community})


def join_community(request):
    template_name = 'accounts/join_community.html'
    if request.method == 'POST':
        form = JoinCommunityForm(request.POST)
        if form.is_valid():
            community_id = form.cleaned_data['community_id']
            community = Community.objects.get(id=community_id)
            user = request.user
            user.communities.add(community)
            return redirect('accounts:community_list')
    else:
        form = JoinCommunityForm()
    return render(request, template_name, {'form': form})


def register_new_user(request):
    template_name = 'accounts/new_user_template.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:profile')  # Redirect to user profile or another page
    else:
        form = UserCreationForm()
    return render(request, template_name, {'form': form})


@login_required
def profile_view(request):
    # Check if the user is logged in through Google or a local account
    try:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('accounts:profile')  # Redirect back to profile page

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        # Check for Google profile picture (if the user is logged in with Google)
        if hasattr(request.user, 'socialaccount_set'):
            social_account = SocialAccount.objects.filter(user=request.user, provider='google').first()
            if social_account:
                profile_picture = social_account.get_avatar_url()  # Get Google profile picture URL
            else:
                # Fallback to local user profile picture
                profile_picture = request.user.profile.avatar.url if request.user.profile.avatar.url else None
        else:
            # User is logged in with a local account, show local profile picture
            profile_picture = request.user.profile.avatar.url if request.user.profile.avatar.url else None

        # If user is not logged in, show the public profile picture of the other user (viewing other's profile)
        if not request.user.is_authenticated:
            profile_picture = request.user.profile.profile_picture.url if request.user.profile.profile_picture else None

        # Prepare context for rendering the profile page
        context = {
            'u_form': u_form,
            'p_form': p_form,
            'profile_picture': profile_picture
        }

        return render(request, 'accounts/profile.html', context)

    except User.DoesNotExist:
        # Handle case where user does not exist
        messages.error(request, "User not found!")
        return redirect('dashboard:dashboard')  # Redirect to home page or error page


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('accounts:profile')  # Redirect to home or any other page
        else:
            return redirect('accounts:profile')
    else:
        form = UserProfileForm()

    return render(request, 'accounts/profile.html', {'form': form})


def upload_profile_photo(request):
    template_name = 'accounts/upload_profile.html'
    return render(request, template_name)


def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')  # Redirect to profile page after saving
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


def accounts(request):
    template_name = 'accounts/accounts.html'
    return render(request, template_name)


@login_required
def profile_edit(request):
    p_edit = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'form': form})


def activity_log(request):
    template_name = 'accounts/activity_log.html'
    return render(request, template_name)


def contact_support(request):
    template_name = 'accounts/contact_support.html'
    return render(request, template_name)
