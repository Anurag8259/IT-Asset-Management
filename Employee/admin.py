from django.contrib import admin
from .models import Employees
# Register your models here.
class UserForm(admin.ModelAdmin):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['employee_name'].required=True
class UserAdmin(admin.ModelAdmin):
    list_display=('employee_name','employee_code')
admin.site.register(Employees,UserAdmin)