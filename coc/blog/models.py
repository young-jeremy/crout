from django.conf import settings
from django.db import models
from django.db.models.signals import post_save



class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(blank=True, null=True)
    date_published=models.DateField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )


    def __str__(self):
        return str(self.title)

    def post_save_receiver(sender, instance, created, **kwargs):
        pass

    post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)