from django.contrib import admin
from software.models import Software
# Register your models here.
class SoftwareForm(admin.ModelAdmin):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['software_name','validity'].required=True
class SoftwareAdmin(admin.ModelAdmin):
    list_display=('software_name','buy_date','price','version','vendor','validity')

admin.site.register(Software,SoftwareAdmin)


