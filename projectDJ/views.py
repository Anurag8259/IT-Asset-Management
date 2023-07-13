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
def userRole(req):
        pdata=PC.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        prdata=Printer.objects.all()
        nddata=NetworkDevice.objects.all()
        mdata=MiscDevice.objects.all()
        udata=User.objects.all()
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
            'udata':udata,
            'mdata':mdata,
            'nddata':nddata,
            'prdata':prdata,
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        
        return render(req,"userRole.html",data)
def LoginPage(req):
    req.session.flush()
    logout(req)
    if req.method=='GET':
        return render(req,"login.html")
    if req.method=='POST':
        usr=req.POST.get("username")
        pwd=req.POST.get("password")
        user=authenticate(req,username=usr,password=pwd)
        if user is not None:
            login(req,user)
            return HttpResponseRedirect("/dashboard")

    return HttpResponse("Wrong credentials")
@login_required
def DashboardPage(req):
        pdata=PC.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        prdata=Printer.objects.all()
        nddata=NetworkDevice.objects.all()
        mdata=MiscDevice.objects.all()
        udata=User.objects.all()
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
            'udata':udata,
            'mdata':mdata,
            'nddata':nddata,
            'prdata':prdata,
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        
        return render(req,"dashboard.html",data)




        
def Logout(request):
    logout(request)
    return render('login.html')
def RequestPage(req):
    if req.method == 'POST':
        
        
        action = req.POST.get('action')

        # if action == 'accept_emp':
        #     employeeId = req.POST.get('employee_id')
        #     t=Employees.objects.get(id=employeeId)
        #     t.status="approved"
        #     t.save()
        if action == 'accept_pc':
            pcid=req.POST.get('pc_id')
            t=PC.objects.get(id=pcid)
            t.status="approved"
            t.save()
        if action == 'accept_printer':
            pcid=req.POST.get('printer_id')
            t=Printer.objects.get(id=pcid)
            t.status="approved"
            t.save()
        if action == 'accept_nd':
            pcid=req.POST.get('nd_id')
            t=NetworkDevice.objects.get(id=pcid)
            t.status="approved"
            t.save()
        if action == 'accept_misc':
            pcid=req.POST.get('misc_id')
            t=MiscDevice.objects.get(id=pcid)
            t.status="approved"
            t.save()
            


        
        # if action == 'reject_emp':
        #     employeeId = req.POST.get('employee_id')
        #     t=Employees.objects.get(id=employeeId)
        #     t.status="rejected"
        #     t.save()
        if action == 'reject_pc':
            pcid=req.POST.get('pc_id')
            t=PC.objects.get(id=pcid)
            t.status="rejected"
            t.save()
        if action == 'reject_printer':
            pcid=req.POST.get('printer_id')
            t=Printer.objects.get(id=pcid)
            t.status="rejected"
            t.save()
        if action == 'reject_nd':
            pcid=req.POST.get('nd_id')
            t=NetworkDevice.objects.get(id=pcid)
            t.status="rejected"
            t.save()
        if action == 'reject_misc':
            pcid=req.POST.get('misc_id')
            t=MiscDevice.objects.get(id=pcid)
            t.status="rejected"
            t.save()
            
            
        pdata=PC.objects.all()
        edata=Employees.objects.all()
        ldata=Location.objects.all()
        sdata=Software.objects.all()
        prdata=Printer.objects.all()
        nddata=NetworkDevice.objects.all()
        mdata=MiscDevice.objects.all()
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
            'mdata':mdata,
            'nddata':nddata,
            'prdata':prdata,
            'pdata':pdata,
            'ldata':ldata,
            'sdata':sdata,
            'edata':edata
        }
        
        return render(req,"request.html",data)
    pdata=PC.objects.all()
    edata=Employees.objects.all()
    ldata=Location.objects.all()
    sdata=Software.objects.all()
    prdata=Printer.objects.all()
    nddata=NetworkDevice.objects.all()
    mdata=MiscDevice.objects.all()
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
        'mdata':mdata,
        'nddata':nddata,
        'prdata':prdata,
        'pdata':pdata,
        'ldata':ldata,
        'sdata':sdata,
        'edata':edata
    }
    return render(req,"request.html",data)

def CreateUserPage(req):
    if req.method=='POST':
        username = req.POST['username']
        password = req.POST['password']
        confirm_password = req.POST['confirm_password']
        role = req.POST['role']
        loc=req.POST['location']
        
        if password == confirm_password:
            # Create the user
            user = User.objects.create_user(username=username, password=password)
            # users = req.user
            # users.myuser.role=role
            # Set the role (assuming you have a UserProfile model with a OneToOne relation to User)
            # user.myuser.role = role
            myuser=MyUser.objects.create(user=user,role=role,location_id=loc)
            user.save()
            myuser.save()
            return redirect("login")
        else:
            return render(req, 'userForm.html', {'error': 'Passwords do not match.'})
    pdata=PC.objects.all()
    edata=Employees.objects.all()
    ldata=Location.objects.all()
    sdata=Software.objects.all()
    prdata=Printer.objects.all()
    nddata=NetworkDevice.objects.all()
    mdata=MiscDevice.objects.all()
    data={
        'mdata':mdata,
        'nddata':nddata,
        'prdata':prdata,
        'pdata':pdata,
        'ldata':ldata,
        'sdata':sdata,
        'edata':edata
    }
    return render(req, 'userForm.html',data)







def export(req):
    response=HttpResponse(content_type='text/csv')

    writer=csv.writer(response)

    writer.writerow(['PC'])
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

    writer.writerow(['Printer'])
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

    writer.writerow(['Softwares'])
    writer.writerow(['Software Name', 'Buy Date', 'Price', 'Version', 'Vendor', 'Validity'])

    softwares = Software.objects.all()
    for software in softwares:
        writer.writerow([
            software.software_name,
            software.buy_date,
            software.price,
            software.version,
            software.vendor,
            software.get_validity_display()  # Get the display value for the validity field
        ])
    response['Content-Disposition']='attachment; filename="AssetManagement.csv"'
    return response


