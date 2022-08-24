# Generated by Django 3.2.14 on 2022-08-16 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='to_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]