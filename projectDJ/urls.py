"""
URL configuration for projectDJ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# admin.site.index_template = 'hardware.html'
# admin.autodiscover()
admin.site.index_template = 'admin/my_custom_index.html'
admin.autodiscover()
from django.urls import path
from projectDJ import views
from pc import views as pcviews
from Employee import views as empviews
from location import views as locviews
from printer import views as printerviews
from network_device import views as ndviews
from miscellaneous_device import views as miscviews
from software import views as sofviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('software/',sofviews.SoftwarePage),
    path('location/',locviews.LocationPage),
    path('employee/',empviews.EmployeePage,name="employee_page"),
    path('pc/',pcviews.PCPage,name="pc_page"),
    path('printer/',printerviews.PrinterPage,name="printer_page"),
    path('networkDevice/',ndviews.NetworkDevicePage,name="nd_page"),
    path('miscDevice/',miscviews.MiscDevicePage,name="misc_page"),
    path('',views.LoginPage,name="login"),
    path('create_user/',views.CreateUserPage,name="create_user"),
    path('request/',views.RequestPage,name="request_page"),
    path('dashboard/',views.DashboardPage),
    path('edit/PC/<str:asset_id>/',pcviews.pc_edit),
    path('delete/PC/<str:asset_id>/',pcviews.pc_delete),
    path('edit/Printer/<int:asset_id>/',printerviews.printer_edit),
    path('delete/Printer/<int:asset_id>/',printerviews.printer_delete),
    path('edit/nd/<int:asset_id>/',ndviews.nd_edit),
    path('delete/nd/<int:asset_id>/',ndviews.nd_delete),
    path('edit/misc/<int:asset_id>/',miscviews.misc_edit),
    path('delete/misc/<int:asset_id>/',miscviews.misc_delete),
    path('exportpc/',pcviews.exportpc),
    path('exportnd/',ndviews.exportnd),
    path('exportmisc/',miscviews.exportmisc),
    path('exportsof/',sofviews.exportsof),
    path('exportprinter/',printerviews.exportprinter),
    path('export/',views.export),
    path('userRole/',views.userRole),
    path('upload/', sofviews.readcsv, name='upload_csv'),
    # path('course/<courseid>',views.courseDetails),
]
