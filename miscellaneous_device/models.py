from location.models import Location
from Employee.models import Employees
from django.db import models

import datetime
# Create your models here.
class MiscDevice(models.Model):
    asset_id=models.CharField(max_length=6,null=True)
    device_name=models.CharField(max_length=20,null=True)
    desc=models.CharField(max_length=50)
    location=models.ForeignKey(Location,on_delete=models.PROTECT,null=True)
    serial_no=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    make=models.CharField(max_length=20)
    catagory=models.CharField(max_length=20,null=True)
    price=models.CharField(max_length=15)
    buy_date=models.DateField(default=datetime.date.today)
    warranty=models.IntegerField()
    expiry = models.DateField(null=True, blank=True)
    ip_address=models.CharField(max_length=20)
    status=models.CharField(max_length=50,null=True)
    employee=models.ForeignKey(Employees,on_delete=models.PROTECT,null=True)


    # def save(self, *args, **kwargs):
    #     # Calculate expiry based on buy_date and warranty
    #     if self.buy_date and self.warranty:
    #         self.expiry = self.buy_date + datetime.timedelta(days=self.warranty * 365)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.asset_id