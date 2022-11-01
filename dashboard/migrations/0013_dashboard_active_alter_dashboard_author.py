# Generated by Django 4.1.2 on 2022-11-01 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_dashboard_descraption'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tanla', to=settings.AUTH_USER_MODEL),
        ),
    ]
