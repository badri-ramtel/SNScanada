# Generated by Django 5.0.4 on 2024-04-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0011_rename_country_event_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createevent',
            options={'verbose_name_plural': 'Create New Event'},
        ),
        migrations.RenameField(
            model_name='createevent',
            old_name='name',
            new_name='event_name',
        ),
        migrations.AddField(
            model_name='createevent',
            name='event_created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterModelTable(
            name='createevent',
            table='Create New Event',
        ),
    ]
