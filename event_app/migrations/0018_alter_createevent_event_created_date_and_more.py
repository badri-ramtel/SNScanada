# Generated by Django 5.0.3 on 2024-05-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0017_alter_createevent_event_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createevent',
            name='event_created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
