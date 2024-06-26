# Generated by Django 5.0.3 on 2024-05-19 21:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_adversite_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adversite',
            name='name',
        ),
        migrations.RemoveField(
            model_name='adversite',
            name='picture',
        ),
        migrations.AlterField(
            model_name='adversite',
            name='content',
            field=models.FileField(null=True, upload_to='videos/advertisement/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
