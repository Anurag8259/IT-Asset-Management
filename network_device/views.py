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
def NetworkDevicePage(req):
    if req.method=='GET':
        pdata=PC.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        prdata=Printer.objects.all()
        nddata=NetworkDevice.objects.all()
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
            'nddata':nddata,
            'prdata':prdata,
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        return render(req,"NetworkDevice.html",data)
    if req.method=='POST':
        ai=req.POST.get('assetId')
        name=req.POST.get('networkDevice')
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
        new_block=NetworkDevice.objects.create(asset_id=ai,expiry=expiry,device_name=name,desc=de,location_id=loc,serial_no=sn,model=m,make=mk,catagory=tp,price=pr,buy_date=bd,warranty=war,status=st,employee_id=emp)
        new_block.save()
        pdata=PC.objects.all()
        prdata=Printer.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        nddata=NetworkDevice.objects.all()
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
            'nddata':nddata,
            'prdata':prdata,
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        return render(req,"NetworkDevice.html",data)
    
# NetworkDevice Edit and Delete Functions
def nd_edit(request, asset_id):
    # Retrieve the NetworkDevice object based on the asset_id
    network_device = NetworkDevice.objects.get(id=asset_id)
    
    if request.method == 'POST':
        # Update the NetworkDevice object with the submitted form data
        network_device.device_name = request.POST.get('device_name')
        network_device.desc = request.POST.get('desc')
        network_device.serial_no = request.POST.get('serial_no')
        network_device.model = request.POST.get('model')
        network_device.make = request.POST.get('make')
        network_device.catagory = request.POST.get('catagory')
        network_device.price = request.POST.get('price')
        network_device.warranty = request.POST.get('warranty')


        network_device.ip_address = request.POST.get('ip_address')
        # network_device.status = request.POST.get('status')

        network_device.save()

        return redirect('nd_page')  # Redirect to the NetworkDevice page or another appropriate page
    ldata=Location.objects.all()

    return render(request, 'edit_nd.html', {'network_device': network_device,'loc':ldata})

def nd_delete(request, asset_id):
    # Retrieve the NetworkDevice object based on the asset_id
    network_device = NetworkDevice.objects.get(id=asset_id)
    network_device.delete()

    return redirect('nd_page')





def exportnd(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="network_device_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Network Devices'])
    writer.writerow(['Asset ID', 'Device Name', 'Description', 'Location', 'Serial Number', 'Model', 'Make',
                     'Category', 'Price', 'Buy Date', 'Warranty', 'IP Address', 'Status', 'Employee'])

    network_devices = NetworkDevice.objects.all()
    for device in network_devices:
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
