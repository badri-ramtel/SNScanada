# Generated by Django 5.0.4 on 2024-05-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_president_image_alter_slider_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='president',
            name='image',
            field=models.ImageField(upload_to='images/president/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='picture',
            field=models.ImageField(upload_to='images/slider/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='sub_title',
            field=models.CharField(max_length=254),
        ),
    ]
