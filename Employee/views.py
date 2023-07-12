from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from myuser .models import MyUser
from miscellaneous_device.models import MiscDevice
from network_device.models import NetworkDevice
from printer.models import Printer
from pc.models import PC
import csv
from software.models import Software
from location.models import Location
from Employee.models import Employees
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
flag=2



@login_required
def EmployeePage(req):
    if req.method=='GET':
        edata=Employees.objects.all()
        flag=3
        if req.user.is_authenticated:
            user = req.user
            if hasattr(user, 'myuser'):
                role = user.myuser.role
                if role=='superadmin':
                    flag=0
                elif role=='admin':
                    flag=1
                elif role=='itmanager':
                    flag=2
                elif role=='employee':
                    flag=3
        data={
            'flag':flag,
            'edata':edata
        }
        return render(req,"employee.html",data)
    if req.method=='POST':
        name=req.POST.get('employee')
        ec=req.POST.get('employee_code')
        if req.user.is_superuser:
            st="active"
        else:
            st="pending"
        # st=req.POST.get('status')
        new_block=Employees.objects.create(employee_name=name,employee_code=ec,status=st)
        new_block.save()
        edata=Employees.objects.all()
        if req.user.is_authenticated:
            user = req.user
            if hasattr(user, 'myuser'):
                role = user.myuser.role
                if role=='superadmin':
                    flag=0
                elif role=='admin':
                    flag=1
                elif role=='itmanager':
                    flag=2
                elif role=='employee':
                    flag=3
        data={
            'flag':flag,
            'edata':edata
        }
        return render(req,"employee.html",data)