# Generated by Django 4.1 on 2022-09-08 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0008_geturl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webimage',
            name='username',
        ),
    ]
