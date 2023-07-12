from django.contrib import admin
from network_device.models import NetworkDevice
class NetworkDeviceForm(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['device_name','desc','asset_id'].required=True
class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display=('id','asset_id','device_name','desc','location','serial_no','model','make','catagory','price','buy_date','warranty','status','employee')
admin.site.register(NetworkDevice,NetworkDeviceAdmin)