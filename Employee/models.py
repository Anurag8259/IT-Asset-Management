
from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_name=models.CharField(max_length=50)
    employee_code=models.CharField(max_length=6)
    def __str__(self):
        return self.employee_name