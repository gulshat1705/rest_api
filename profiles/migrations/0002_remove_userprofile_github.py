# Generated by Django 3.2.9 on 2022-01-25 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='github',
        ),
    ]