

from django.db import models
valid_choice=[
    ('yearly','Yearly'),
    ('lifetime','Lifetime'),
    ('monthly','Monthly')
]
class File(models.Model):
    file=models.FileField(upload_to="files")

class Software(models.Model):
    software_name=models.CharField(max_length=50)
    buy_date=models.DateField()
    price=models.CharField(max_length=15,default=0)
    version=models.CharField(max_length=50,default='NA')
    vendor=models.CharField(max_length=50,default='NA')
    validity=models.CharField(max_length=50,choices=valid_choice,default='Lifetime')
    
    def __str__(self):
        return self.software_name
    
    