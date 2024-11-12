from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        super().pre_social_login(request, sociallogin)
        if sociallogin.is_existing:
            user = sociallogin.user
            extra_data = sociallogin.account.extra_data

            # Store the Google username and picture URL
            user.google_username = extra_data.get('name')
            user.google_picture = extra_data.get('picture')
            user.save()
