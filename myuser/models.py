from django.db import models
from location.models import Location
from django.contrib.auth.models import AbstractUser,User
# class MyUser(AbstractUser):
#     class Role(models.TextChoices):
#         SUPERADMIN='SUPERADMIN','Superadmin'
#         ADMIN = 'ADMIN', 'Admin'
#         EMPLOYEE='EMPLOYEE','Employee'

#     base_role=Role.EMPLOYEE
#     # username=models.CharField(max_length=50,primary_key=True)
#     # password=models.CharField(max_length=50)
#     role=models.CharField(max_length=50)


#     def save(self,*args,**kwargs):
#         if not self.pk:
#             self.role=self.base_role
#             return super().save(*args,**kwargs)
# class Employee(User):
#     base_role=MyUser.Role.EMPLOYEE
#     class Meta:
#         proxy=True
role_choice=(
    ('superadmin',"Super Admin"),
    ("admin","Admin"),
    ("itmanager","IT Manager"),
    ("employee", "Employee")
)
class MyUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    role=models.CharField(max_length=20,choices=role_choice)
    location=models.ForeignKey(Location,on_delete=models.PROTECT,null=True)
