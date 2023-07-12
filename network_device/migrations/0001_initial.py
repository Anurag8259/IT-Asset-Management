# Generated by Django 4.2.1 on 2023-07-01 02:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.CharField(max_length=6, null=True)),
                ('device_name', models.CharField(max_length=20, null=True)),
                ('desc', models.CharField(max_length=50)),
                ('serial_no', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('make', models.CharField(max_length=20)),
                ('catagory', models.CharField(max_length=20, null=True)),
                ('price', models.CharField(max_length=15)),
                ('buy_date', models.DateField(default=datetime.date.today)),
                ('warranty', models.IntegerField()),
                ('ip_address', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=50, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Employee.employees')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='location.location')),
            ],
        ),
    ]