from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
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
# Create your views here.
@login_required

def PCPage(req):
    if req.method=='GET':
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        pdata=PC.objects.all()
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
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        return render(req,"pc.html",data)
    if req.method== 'POST':
        name = req.POST.get('hardware')
        locid=req.POST.get("location")
        cp=req.POST.get('cost')
        bd=req.POST.get('buyDate')
        warr=req.POST.get('warranty')
        emptid=req.POST.get("employee")        
        ai=req.POST.get('assetId')
        sn=req.POST.get('serialNo')
        m=req.POST.get('model')
        st=req.POST.get('status')
        mk=req.POST.get('make')
        rm=req.POST.get('ram')
        hd=req.POST.get('hdd')
        cat=req.POST.get('catagory')
        os=req.POST.get('os')
        c=req.POST.get('cpu')
        ip=req.POST.get('ipAddress')
        war=int(warr)
        buy_date = datetime.datetime.strptime(bd, '%Y-%m-%d').date()
        expiry = buy_date + timedelta(days=war * 365)
        sofname=[x.software_name for x in Software.objects.all()]
        sofid=[]
        for x in sofname:
            sofid.append(int(req.POST.get(x))) if req.POST.get(x) else print("Null")

        new_block=PC.objects.create(pc_name=name,expiry=expiry,location_id=locid,price=cp,buy_date=bd,warranty=war,employee_id=emptid,status=st,asset_id=ai,serial_no=sn,model=m,make=mk,ram=rm,hdd=hd,catagory=cat,cpu=c,operating_system=os,ip_address=ip)
        for x in sofid:
            new_block.softwares.add(Software.objects.get(id=x))
        new_block.save()
        pdata=PC.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        pdata=PC.objects.all()
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
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        return render(req,"pc.html",data)




def pc_edit(request, asset_id):
    pc = PC.objects.get(asset_id=asset_id)
    if request.method == 'POST':
        pc.pc_name = request.POST.get('pc_name')
        pc.serial_no = request.POST.get('serial_no')
        pc.model = request.POST.get('model')
        pc.make = request.POST.get('make')
        pc.ram = request.POST.get('ram')
        pc.hdd = request.POST.get('hdd')
        pc.catagory = request.POST.get('catagory')
        pc.operating_system = request.POST.get('operating_system')
        pc.cpu = request.POST.get('cpu')
        pc.ip_address = request.POST.get('ip_address')
        pc.price = request.POST.get('price')
        pc.warranty = request.POST.get('warranty')
        pc.save()

  
        return redirect('pc_page')  # Redirect to the table view or another appropriate page

    ldata=Location.objects.all()
    return render(request, 'edit_pc.html', {'pc': pc,'loc':ldata})

def pc_delete(request, asset_id):
    pc = PC.objects.get(asset_id=asset_id)
    pc.delete()

 
    return redirect('pc_page') 



def exportpc(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pc_data.csv"'

    writer = csv.writer(response)
    
    writer.writerow(['PC'])
    writer.writerow(['PC Name', 'Asset ID', 'Serial Number', 'Model', 'Make', 'RAM', 'HDD', 'Category',
                     'Operating System', 'CPU', 'IP Address', 'Location', 'Price', 'Buy Date', 'Warranty',
                     'Status', 'Employee', 'Software'])

    pcs = PC.objects.all()
    for pc in pcs:
        software_names = pc.get_software()
        writer.writerow([
            pc.pc_name,
            pc.asset_id,
            pc.serial_no,
            pc.model,
            pc.make,
            pc.ram,
            pc.hdd,
            pc.catagory,
            pc.operating_system,
            pc.cpu,
            pc.ip_address,
            pc.location.location_name if pc.location else '',  # Assuming the Location model has a 'name' field
            pc.price,
            pc.buy_date,
            pc.warranty,
            pc.status,
            pc.employee.employee_name if pc.employee else '',  # Assuming the Employees model has a 'name' field
            software_names
        ])

    return response



