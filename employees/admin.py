from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Employee


class EmployeeAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (_('TX::Employees'), {'fields': ('birthdate',('departament','role'), 'boss', 'is_hired', 'traveling_data')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'departament', 'role', 'hired_date']
    list_filter = ('departament', 'role') + UserAdmin.list_filter

admin.site.register(Employee, EmployeeAdmin)