# Generated by Django 4.1.2 on 2022-11-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0011_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
