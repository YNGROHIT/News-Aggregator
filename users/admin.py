from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # The fields to be used in displaying the CustomUser model.
    list_display = ('email', 'first_name', 'last_name', 'phone', 'country', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    # Exclude date_joined field from being editable
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'country')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ()}),  # Remove date_joined
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'country', 'is_active', 'is_staff')}
        ),
    )
    filter_horizontal = ('groups', 'user_permissions')

# Register CustomUser with the custom UserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
