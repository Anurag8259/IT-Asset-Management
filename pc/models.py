import datetime
from django.db import models
from django.utils import timezone
from location.models import Location
from software.models import Software
from Employee.models import Employees

class PC(models.Model):
    pc_name = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=6)
    serial_no = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    make = models.CharField(max_length=20)
    ram = models.CharField(max_length=10)
    hdd = models.CharField(max_length=10)
    catagory = models.CharField(max_length=20)
    operating_system = models.CharField(max_length=20)
    cpu = models.CharField(max_length=10)
    ip_address = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True)
    price = models.CharField(max_length=15)
    buy_date = models.DateField(default=datetime.date.today)
    warranty = models.IntegerField()
    expiry = models.DateField(null=True, blank=True)  # New field for expiry
    status = models.CharField(max_length=50, null=True)
    employee = models.ForeignKey(Employees, on_delete=models.PROTECT, null=True)
    softwares = models.ManyToManyField(Software)

    def get_software(self):
        return ", ".join([p.software_name for p in self.softwares.all()])

    # def save(self, *args, **kwargs):
    #     # Calculate expiry based on buy_date and warranty
    #     if self.buy_date and self.warranty:
    #         self.expiry = self.buy_date + datetime.timedelta(days=self.warranty * 365)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.asset_id
