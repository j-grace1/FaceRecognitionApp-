# Generated by Django 4.1 on 2022-09-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_webimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images')),
            ],
        ),
    ]
