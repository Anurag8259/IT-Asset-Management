from django.contrib import admin
from pc.models import PC
# Register your models here.
class PCForm(admin.ModelAdmin):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['pc_name','employee','status'].required=True
class PCAdmin(admin.ModelAdmin):
    list_display=('pc_name','asset_id','serial_no','model','make','ram','hdd','catagory','operating_system','cpu','ip_address','buy_date','employee','price','warranty','status','get_software')

# model_list=[Hardware,Softwares]
admin.site.register(PC,PCAdmin)
    
# admin.site.register(Hardware,HardwareAdmin)
