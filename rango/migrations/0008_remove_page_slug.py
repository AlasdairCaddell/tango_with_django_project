# Generated by Django 2.2.17 on 2021-02-12 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_page_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
