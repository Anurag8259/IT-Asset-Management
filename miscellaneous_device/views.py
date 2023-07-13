from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from myuser .models import MyUser
from miscellaneous_device.models import MiscDevice
from network_device.models import NetworkDevice
from printer.models import Printer
from pc.models import PC
import csv
import datetime
from datetime import timedelta
from software.models import Software
from location.models import Location
from Employee.models import Employees
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
flag=2


@login_required
def MiscDevicePage(req):
    if req.method=='GET':
        pdata=PC.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        prdata=Printer.objects.all()
        nddata=NetworkDevice.objects.all()
        mdata=MiscDevice.objects.all()
        flag=3
        loc=""
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
                    loc=user.myuser.location
                elif role=='employee':
                    flag=3
        data={
            'loc':loc,
            'flag':flag,
            'mdata':mdata,
            'nddata':nddata,
            'prdata':prdata,
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        return render(req,"misc.html",data)
    if req.method=='POST':
        ai=req.POST.get('assetId')
        name=req.POST.get('device')
        de=req.POST.get('desc')
        loc=req.POST.get('location')
        sn=req.POST.get('serialNo')
        m=req.POST.get('model')
        mk=req.POST.get('make')
        tp=req.POST.get('catagory')
        pr=req.POST.get('price')
        bd=req.POST.get('buyDate')
        warr=req.POST.get('warranty')
        st=req.POST.get('status')
        emp=req.POST.get('employee')
        war=int(warr)
        buy_date = datetime.datetime.strptime(bd, '%Y-%m-%d').date()
        expiry = buy_date + timedelta(days=war * 365)
        new_block=MiscDevice.objects.create(asset_id=ai,expiry=expiry,device_name=name,desc=de,location_id=loc,serial_no=sn,model=m,make=mk,catagory=tp,price=pr,buy_date=bd,warranty=war,status=st,employee_id=emp)
        new_block.save()
        pdata=PC.objects.all()
        prdata=Printer.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        nddata=NetworkDevice.objects.all()
        mdata=MiscDevice.objects.all()
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
                    loc=user.myuser.location
                elif role=='employee':
                    flag=3
        data={
            'loc':loc,
            'flag':flag,
            'mdata':mdata,
            'nddata':nddata,
            'prdata':prdata,
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        return render(req,"misc.html",data)
    

# MiscDevice Edit and Delete Functions
def misc_edit(request, asset_id):
    # Retrieve the MiscDevice object based on the asset_id
    misc_device = MiscDevice.objects.get(id=asset_id)
    
    if request.method == 'POST':
        # Update the MiscDevice object with the submitted form data
        misc_device.device_name = request.POST.get('device_name')
        misc_device.desc = request.POST.get('desc')
        misc_device.serial_no = request.POST.get('serial_no')
        misc_device.model = request.POST.get('model')
        misc_device.make = request.POST.get('make')
        misc_device.catagory = request.POST.get('catagory')
        misc_device.price = request.POST.get('price')
        misc_device.warranty = request.POST.get('warranty')
        misc_device.ip_address = request.POST.get('ip_address')
        # misc_device.status = request.POST.get('status')

        misc_device.save()

        return redirect('misc_page')  # Redirect to the MiscDevice page or another appropriate page
    ldata=Location.objects.all()
    return render(request, 'edit_misc.html', {'misc_device': misc_device,'loc':ldata})

def misc_delete(request, asset_id):
    # Retrieve the MiscDevice object based on the asset_id
    misc_device = MiscDevice.objects.get(id=asset_id)
    misc_device.delete()

    return redirect('misc_page')




def exportmisc(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="misc_device_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Miscellaneous Devices'])
    writer.writerow(['Asset ID', 'Device Name', 'Description', 'Location', 'Serial Number', 'Model', 'Make',
                     'Category', 'Price', 'Buy Date', 'Warranty', 'IP Address', 'Status', 'Employee'])

    misc_devices = MiscDevice.objects.all()
    for device in misc_devices:
        writer.writerow([
            device.asset_id,
            device.device_name,
            device.desc,
            device.location.location_name if device.location else '',  # Assuming the Location model has a 'name' field
            device.serial_no,
            device.model,
            device.make,
            device.catagory if device.catagory else '',  # Assuming the 'category' field is nullable
            device.price,
            device.buy_date,
            device.warranty,
            device.ip_address,
            device.status,
            device.employee.employee_name if device.employee else ''  # Assuming the Employees model has a 'name' field
        ])

    return response
