from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form = UserForm
    model = User
    list_display = ('full_name','email','phone', 'is_superuser','is_active')
    list_filter = ('full_name','email','phone','is_superuser', 'is_active','date_joined')
    fieldsets = (
        (None, {'fields': ('full_name','email','phone','address','is_superuser', 'last_login',"date_joined")}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name','email','phone','address', 'password1', 'password2', 'is_staff', 'is_active', 'last_login',"date_joined")}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)
admin.site.register(User,UserAdmin)