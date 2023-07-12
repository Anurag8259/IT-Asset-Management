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
def LocationPage(req):
        if req.method=='GET':
            ldata=Location.objects.all()
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
                'ldata':ldata
            }
            return render(req,"location.html",data)
        if req.method=='POST':
            name=req.POST.get('location')
            # pin=req.POST.get('pincode')
            new_block=Location.objects.create(location_name=name)
            new_block.save()
            ldata=Location.objects.all()
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
                'ldata':ldata
            }
            return render(req,"location.html",data)