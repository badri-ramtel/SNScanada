# Generated by Django 5.0.4 on 2024-04-30 18:07

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0015_rename_paragraph_1_about_about_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_content',
            field=tinymce.models.HTMLField(),
        ),
    ]
