from django.contrib import admin
from .models import Location
# Register your models here.
class LocationForm(admin.ModelAdmin):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['location_name'].required=True

class LocationAdmin(admin.ModelAdmin):
    list_display=('id','location_name')
admin.site.register(Location,LocationAdmin)


