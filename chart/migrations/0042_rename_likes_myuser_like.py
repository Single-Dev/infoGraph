# Generated by Django 4.1.2 on 2022-12-25 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0041_myuser_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='likes',
            new_name='like',
        ),
    ]
