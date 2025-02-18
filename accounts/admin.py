from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ConstructionManager, PersonConstructionManager, CompanyConstructionManager

# Custom admin class for ConstructionManager to show custom fields
class ConstructionManagerAdmin(UserAdmin):
    model = ConstructionManager
    list_display = ('email', 'phone_number', 'is_staff', 'is_superuser')
    search_fields = ('email', 'phone_number')
    ordering = ('email',)

    # Specifying the fields to display and edit
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('phone_number', 'district_1st', 'district_2nd', 'district_3rd', 'district_4th', 'district_5th', 'min_floors', 'max_floors', 'min_area', 'max_area')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2', 'district_1st', 'district_2nd', 'district_3rd', 'district_4th', 'district_5th', 'min_floors', 'max_floors', 'min_area', 'max_area', 'is_staff', 'is_active')
        }),
    )
    filter_horizontal = ('groups', 'user_permissions',)

# Registering PersonConstructionManager with same fields as ConstructionManagerAdmin
class PersonConstructionManagerAdmin(ConstructionManagerAdmin):
    model = PersonConstructionManager

# Registering CompanyConstructionManager with a custom display for the name field
class CompanyConstructionManagerAdmin(ConstructionManagerAdmin):
    model = CompanyConstructionManager
    list_display = ('email', 'name', 'phone_number', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Company Info', {'fields': ('name', 'phone_number', 'district_1st', 'district_2nd', 'district_3rd', 'district_4th', 'district_5th', 'min_floors', 'max_floors', 'min_area', 'max_area')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone_number', 'password1', 'password2', 'district_1st', 'district_2nd', 'district_3rd', 'district_4th', 'district_5th', 'min_floors', 'max_floors', 'min_area', 'max_area', 'is_staff', 'is_active')
        }),
    )

# Registering all the models with their custom admins
admin.site.register(ConstructionManager, ConstructionManagerAdmin)
admin.site.register(PersonConstructionManager, PersonConstructionManagerAdmin)
admin.site.register(CompanyConstructionManager, CompanyConstructionManagerAdmin)
