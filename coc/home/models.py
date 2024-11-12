from django.db import models



class About(models.Model):
    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)
