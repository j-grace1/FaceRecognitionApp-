# Generated by Django 4.1 on 2022-09-04 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_uploadimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimage',
            name='caption',
        ),
    ]
