# Generated by Django 5.0.4 on 2024-05-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0015_alter_event_country_alter_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(upload_to='images/event/'),
        ),
    ]
