# Generated by Django 4.2.14 on 2024-08-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='member_id',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
