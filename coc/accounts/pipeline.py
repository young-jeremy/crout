# your_app/pipeline.py
def save_google_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        user.google_profile_pic = response.get('picture')
        user.save()
