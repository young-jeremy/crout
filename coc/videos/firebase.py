# firebase.py
import firebase_admin
from firebase_admin import credentials
from django.conf import settings


# Initialize Firebase Admin
def initialize_firebase():
    cred = credentials.Certificate(settings.FIRE_BASE_KEY)
#    firebase_admin.initialize_app(cred)
