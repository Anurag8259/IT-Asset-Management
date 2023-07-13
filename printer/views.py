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
def PrinterPage(req):
    if req.method=='GET':
        pdata=PC.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        prdata=Printer.objects.all()
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
            'prdata':prdata,
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        return render(req,"printer.html",data)
    if req.method=='POST':
        ai=req.POST.get('assetId')
        name=req.POST.get('printer')
        de=req.POST.get('desc')
        loc=req.POST.get('location')
        sn=req.POST.get('serialNo')
        m=req.POST.get('model')
        mk=req.POST.get('make')
        tp=req.POST.get('type')
        pr=req.POST.get('price')
        bd=req.POST.get('buyDate')
        warr=req.POST.get('warranty')
        st=req.POST.get('status')
        emp=req.POST.get('employee')
        war=int(warr)
        buy_date = datetime.datetime.strptime(bd, '%Y-%m-%d').date()
        expiry = buy_date + timedelta(days=war * 365)
        new_block=Printer.objects.create(asset_id=ai,printer_name=name,desc=de,location_id=loc,serial_no=sn,model=m,expiry=expiry,make=mk,type=tp,price=pr,buy_date=bd,warranty=war,status=st,employee_id=emp)
        new_block.save()
        pdata=PC.objects.all()
        prdata=Printer.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
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
            'prdata':prdata,
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        return render(req,"printer.html",data)
    
def printer_edit(request, asset_id):
    # Retrieve the Printer object based on the asset_id
    printer = Printer.objects.get(id=asset_id)
    
    if request.method == 'POST':
        # Update the Printer object with the submitted form data
        printer.printer_name = request.POST.get('printer_name')
        printer.desc = request.POST.get('desc')
        printer.serial_no = request.POST.get('serial_no')
        printer.model = request.POST.get('model')
        printer.make = request.POST.get('make')
        printer.type = request.POST.get('type')
        printer.price = request.POST.get('price')
        printer.warranty = request.POST.get('warranty')
        printer.save()

        return redirect('printer_page')  # Redirect to the Printer page or another appropriate page

    ldata=Location.objects.all()
    return render(request, 'edit_printer.html', {'printer': printer,'loc':ldata})

def printer_delete(request, asset_id):
    # Retrieve the Printer object based on the asset_id
    printer = Printer.objects.get(id=asset_id)
    printer.delete()

    return redirect('printer_page')

def exportprinter(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="printer_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Printer'])
    writer.writerow(['Asset ID', 'Printer Name', 'Description', 'Location', 'Serial Number', 'Model', 'Make', 'Type',
                     'Price', 'Buy Date', 'Warranty', 'Status', 'Employee'])

    printers = Printer.objects.all()
    for printer in printers:
        writer.writerow([
            printer.asset_id,
            printer.printer_name,
            printer.desc,
            printer.location.location_name,  # Assuming the Location model has a 'name' field
            printer.serial_no,
            printer.model,
            printer.make,
            printer.type,
            printer.price,
            printer.buy_date,
            printer.warranty,
            printer.status,
            printer.employee.employee_name  # Assuming the Employees model has a 'name' field
        ])

    return response

