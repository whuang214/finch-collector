# Generated by Django 3.2.12 on 2023-08-16 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finch',
            name='average_lifespan',
        ),
        migrations.RemoveField(
            model_name='finch',
            name='native_region',
        ),
        migrations.RemoveField(
            model_name='finch',
            name='scientific_name',
        ),
    ]
