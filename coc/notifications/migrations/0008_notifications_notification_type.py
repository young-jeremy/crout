# Generated by Django 5.1.2 on 2024-11-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_alter_notifications_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='notification_type',
            field=models.CharField(max_length=155, null=True),
        ),
    ]
