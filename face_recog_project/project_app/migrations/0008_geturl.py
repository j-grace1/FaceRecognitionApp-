# Generated by Django 4.1 on 2022-09-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0007_rename_image_webimage_images_webimage_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Url', models.CharField(max_length=4294967295)),
            ],
        ),
    ]
