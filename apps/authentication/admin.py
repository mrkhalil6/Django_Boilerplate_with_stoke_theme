# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Organization


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('User Credentials', {
            'fields': ('email', 'username', 'password', 'first_name', 'last_name', 'phone_number',)
        }),

        ('Basic', {
            'fields': ('unique_code', 'date_of_birth',
                       'user_image', 'type', 'is_super_admin', 'is_organization_admin', 'is_staff', 'is_active',
                       'organization',
                       'last_login', 'date_joined', 'created_by', 'modified_by', 'status',)
        }),
    )
    readonly_fields = ['date_joined']


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Organization)
