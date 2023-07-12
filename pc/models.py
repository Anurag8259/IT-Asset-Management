from location.models import Location
from software.models import Software
from Employee.models import Employees
from django.db import models
from django.utils import timezone


import datetime
# Create your models here.
class PC(models.Model):
    pc_name=models.CharField(max_length=100)
    asset_id=models.CharField(max_length=6)
    serial_no=models.CharField(max_length=20)
    model=models.CharField(max_length=30)
    make=models.CharField(max_length=20)
    ram=models.CharField(max_length=10)
    hdd=models.CharField(max_length=10)
    catagory=models.CharField(max_length=20)
    operating_system=models.CharField(max_length=20)
    cpu=models.CharField(max_length=10)
    ip_address=models.CharField(max_length=20)
    # location=models.OneToOneField(Location,on_delete=models.PROTECT,primary_key=True)
    location=models.ForeignKey(Location,on_delete=models.PROTECT,null=True)
    price=models.CharField(max_length=15)
    buy_date=models.DateField(default=datetime.date.today)
    warranty=models.IntegerField()
    status=models.CharField(max_length=50,null=True)
    employee=models.ForeignKey(Employees,on_delete=models.PROTECT,null=True)
    # employee=models.OneToOneField(Employees,on_delete=models.PROTECT,null=True)
    # employee and location must be a one to many field(error- unique constraint failed)
    softwares=models.ManyToManyField(Software)
    def get_software(self):
        return " , ".join([p.software_name for p in self.softwares.all()])
    # def __str__(self):
    #     return self.asset_id
    