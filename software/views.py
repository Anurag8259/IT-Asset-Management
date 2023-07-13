from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from myuser .models import MyUser
from miscellaneous_device.models import MiscDevice
from network_device.models import NetworkDevice
from printer.models import Printer
from pc.models import PC
import csv
from software.models import Software,File
from location.models import Location
from Employee.models import Employees
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import pandas as pd
flag=2
@login_required
def SoftwarePage(req):
    if req.method=='GET':
        sdata=Software.objects.all()
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
            'sdata':sdata,
        }
        return render(req,"software.html",data)
    if req.method=='POST':
        name=req.POST.get('software')
        bd=req.POST.get('buyDate')
        cp=req.POST.get('cost')
        ver=req.POST.get('version')
        ven=req.POST.get('vendor')
        new_block=Software.objects.create(software_name=name,buy_date=bd,price=cp,version=ver,vendor=ven)
        new_block.save()
        sdata=Software.objects.all()
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
            'sdata':sdata,
        }
        return render(req,"software.html",data)




def exportsof(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="software_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['software_name', 'buy_date', 'price', 'version', 'vendor', 'validity'])

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

    return response

# def upload_csv(request):
#     if request.method == 'POST':
#         csv_file = request.FILES.get('csv_file') 
        
#         if csv_file:
#             decoded_file = csv_file.read().decode('utf-8') 
            
#             # Process the CSV data and create Software objects
#             csv_reader = csv.DictReader(decoded_file.splitlines())
#             for row in csv_reader:
#                 software = Software(
#                     software_name=row['software_name'],
#                     buy_date=row['buy_date'],
#                     price=row['price'],
#                     version=row['version'],
#                     vendor=row['vendor'],
#                     validity=row['validity']
#                 )
#                 software.save()  # Save each Software object to the database

#     return render(request, 'software.html')
def create_db(file_path):
    df=pd.read_csv(file_path,delimiter=',')
    print(df.values)
    list_of_csv=[list(row) for row in df.values]

    for l in list_of_csv:
        Software.objects.create(
                    software_name=l[1],
                    buy_date=l[2],
                    price=l[3],
                    version=l[4],
                    vendor=l[5],
                    validity=l[6]
        )
        Software.save()
def readcsv(req):
    if req.method == "POST":
        file=req.FILES['files']
        obj=File.objects.create(file = file)
        create_db(obj.file)
    return render(req,'software.html')
