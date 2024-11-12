from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from .models import UserProfile

class Command(BaseCommand):
    help = 'Create missing profiles for users'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(profile__isnull=True)
        for user in users_without_profiles:
            UserProfile.objects.create(user=user)
            self.stdout.write(f"Created profile for {user.username}")
