# Generated by Django 5.0.3 on 2024-05-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0016_alter_event_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createevent',
            name='event_created_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
