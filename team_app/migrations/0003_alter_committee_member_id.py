# Generated by Django 4.2.14 on 2024-08-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0002_committee_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='member_id',
            field=models.IntegerField(max_length=100),
        ),
    ]
