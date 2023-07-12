

from django.db import models
valid_choice=[
    ('yearly','Yearly'),
    ('lifetime','Lifetime'),
    ('monthly','Monthly')
]
# Create your models here.
class Software(models.Model):
    software_name=models.CharField(max_length=50)
    buy_date=models.DateField()
    price=models.CharField(max_length=15,default=0)
    version=models.CharField(max_length=50,default='NA')
    vendor=models.CharField(max_length=50,default='NA')
    validity=models.CharField(max_length=50,choices=valid_choice,default='Lifetime')
    
    def __str__(self):
        return self.software_name
    
    # hardware=models.ManyToManyField(hardware.models.Hardware)
#     class Meta:
#         ordering=['software_name']
#     def __str__(self):
#         return self.software_name
# class Hardware(models.Model):
#     hardwares=models.CharField(max_length=50)
#     class Meta:
#         ordering=['hardwares']
#     def __str__(self):
#         return self.hardwares
