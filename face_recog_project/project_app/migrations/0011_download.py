# Generated by Django 4.1 on 2022-09-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0010_remove_person_title_person_address_person_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='download')),
            ],
        ),
    ]
