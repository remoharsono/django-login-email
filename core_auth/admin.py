from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

# Register your models here.
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2'),})
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_field = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    