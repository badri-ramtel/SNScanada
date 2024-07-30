# Generated by Django 4.2.14 on 2024-07-28 16:44

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alertmessagehide'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertmessage',
            name='pic_message',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/alert_message/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alertmessage',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
