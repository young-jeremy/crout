# Generated by Django 5.1.2 on 2024-11-08 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_content_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
