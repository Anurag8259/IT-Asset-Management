from django.contrib import admin
from printer.models import Printer
class PrinterForm(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['printer_name','desc','asset_id'].required=True
class PrinterAdmin(admin.ModelAdmin):
    list_display=('asset_id','printer_name','desc','location','serial_no','model','make','type','price','buy_date','warranty','expiry','status','employee')
admin.site.register(Printer,PrinterAdmin)