# Generated by Django 4.2.1 on 2023-07-05 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_employees_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='status',
        ),
    ]