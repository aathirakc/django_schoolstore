# Generated by Django 3.2.22 on 2024-01-14 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dropdown',
            name='name',
        ),
    ]