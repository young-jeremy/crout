# myapp/apps.py
from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
import os
from .firebase import initialize_firebase



# Initialize Firebase
initialize_firebase()

class VideosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videos'

    def ready(self):
        import videos.signals
        # Initialize Firebase if not already initialized

