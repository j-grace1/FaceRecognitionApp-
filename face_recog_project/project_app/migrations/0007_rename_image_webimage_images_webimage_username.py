# Generated by Django 4.1 on 2022-09-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0006_alter_multipleimage_images_alter_webimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webimage',
            old_name='image',
            new_name='images',
        ),
        migrations.AddField(
            model_name='webimage',
            name='username',
            field=models.CharField(default='some_value', max_length=30),
        ),
    ]
