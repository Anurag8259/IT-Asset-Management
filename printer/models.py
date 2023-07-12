from location.models import Location
from Employee.models import Employees
from django.db import models

import datetime
# Create your models here.
class Printer(models.Model):
    asset_id=models.CharField(max_length=6,null=True)
    printer_name=models.CharField(max_length=20,null=True)
    desc=models.CharField(max_length=50)
    location=models.ForeignKey(Location,on_delete=models.PROTECT,null=True)
    serial_no=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    make=models.CharField(max_length=20)
    type=models.CharField(max_length=20,null=True)
    price=models.CharField(max_length=15)
    buy_date=models.DateField(default=datetime.date.today)
    warranty=models.IntegerField()
    status=models.CharField(max_length=50,null=True)
    employee=models.ForeignKey(Employees,on_delete=models.PROTECT,null=True)