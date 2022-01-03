from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'middle_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Info'), {'fields': ('phone', 'avatar')}),
    )

admin.site.register(UserProfile, UserAdmin)
# Register your models here.
