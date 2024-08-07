# Generated by Django 4.2.14 on 2024-07-22 14:55

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Year_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_frame', models.CharField(max_length=10)),
                ('current_year', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Year Book',
                'db_table': 'Year Book',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submenu', models.CharField(max_length=100)),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='team_app.year_book')),
            ],
            options={
                'verbose_name_plural': 'Sub Menu',
                'db_table': 'Sub Menu',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='images/committees/profile_pic/')),
                ('name', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('bio', tinymce.models.HTMLField()),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='team_app.year_book')),
            ],
            options={
                'verbose_name_plural': 'Committee',
                'db_table': 'Committee',
                'ordering': ['-id'],
            },
        ),
    ]
