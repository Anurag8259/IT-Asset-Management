from django.contrib import admin
from miscellaneous_device.models import MiscDevice
class MiscDeviceForm(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['device_name','desc','asset_id'].required=True
class MiscDeviceAdmin(admin.ModelAdmin):
    list_display=('asset_id','device_name','desc','location','serial_no','model','make','catagory','price','buy_date','warranty','status','employee')
admin.site.register(MiscDevice,MiscDeviceAdmin)