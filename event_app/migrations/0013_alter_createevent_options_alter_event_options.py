# Generated by Django 5.0.4 on 2024-05-13 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0012_alter_createevent_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createevent',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Create New Event'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Event'},
        ),
    ]
