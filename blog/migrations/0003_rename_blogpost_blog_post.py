# Generated by Django 3.2.14 on 2022-08-17 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_picture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Blog_post',
        ),
    ]