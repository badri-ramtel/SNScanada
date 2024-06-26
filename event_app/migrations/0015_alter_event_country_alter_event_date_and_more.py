# Generated by Django 5.0.4 on 2024-05-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0014_alter_event_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='country',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(upload_to='event_images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=200),
        ),
    ]
