# Generated by Django 4.2.1 on 2023-07-03 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='pincode',
        ),
    ]