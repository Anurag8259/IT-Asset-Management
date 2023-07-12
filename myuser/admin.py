from django.contrib import admin
from myuser.models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# class MyUserForm(admin.ModelAdmin):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username','password','role'].required=True
# class MyUserAdmin(admin.ModelAdmin):
#     list_display=('username','password','role')
class UserInline(admin.StackedInline):
    model=MyUser
    can_delete=False
    verbose_name_plural='myuser'
class UserAdmin(BaseUserAdmin):
    inlines=(UserInline,)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)