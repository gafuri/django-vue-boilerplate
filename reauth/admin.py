from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('fio', 'phone', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fio', 'phone', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'fio', 'phone', 'avatar', 'date_joined', 'is_staff', 'is_active')
    search_fields = ('email', 'fio', 'phone', 'avatar', 'is_staff', 'is_active')
    ordering = ('email',)
