from django.conf import settings
# from videos.models import *
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify

from services.models import Channel

# from django.dispatch import receiver
# from django.db.models.signals import post_save



account_type_choices = [
    ('premium_account','PREMIUM_ACCOUNT' ),
    ('regular_account', 'REGULAR_ACCOUNT'),
]


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    google_username = models.CharField(max_length=255, blank=True, null=True)
    google_picture = models.URLField(blank=True, null=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_joined = models.DateField(auto_now=True, blank=True, null=True)
    send_notification_email = models.BooleanField(default=True)




    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]

    def should_notify(self, notification_type):
        if notification_type == 'send_notification_email':
            return self.send_notification_email

    def __str__(self):
        # Example for the User model or Profile model
        return self.username if self.username else "No Username"

    def get_all_permissions(self, perm, obj=None):
        return True


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserProfile(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    school_affiliate = models.CharField(max_length=100, blank=True)
    national_identification_number = models.IntegerField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, blank=True)
    course_of_study = models.CharField(max_length=100, blank=True, null=True)
    current_country_or_residence = models.CharField(max_length=100, blank=True)
    current_county = models.CharField(max_length=100, blank=True)
    current_city = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    level_of_education = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='static/img/undraw_profile_2.svg')
    slug = models.SlugField(unique=True, blank=True)
    receive_newsletter = models.BooleanField(default=False)  # Checkbox
    account_type = models.CharField(max_length=100, choices=account_type_choices, default='regular_account')
    address = models.CharField(max_length=100, blank=True, null=True)
    send_notification_email = models.BooleanField(default=True)


    def __str__(self):
        # Return a string representation of the profile
        return self.user.username if self.user.username else "Unnamed Profile"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super().save(*args, **kwargs)


class ProfileType(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.profile


class RevenueSharingRule(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    percentage_share = models.DecimalField(max_digits=5, decimal_places=2)


class Report (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    reason = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content_type)



