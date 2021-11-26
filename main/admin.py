from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'address')}),
        (_('Permissions'), {
            'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone', 'tg_id', 'tg_username', 'address')
    list_display_links = ('id', 'username')


admin.site.register(Users, UserAdmin)

admin.site.register(Category)
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')
    list_display_links = ('id', 'name')

admin.site.register(Products)
admin.site.register(Shop)
admin.site.register(ShopItems)
admin.site.register(Savatcha)
admin.site.register(SavatchaItems)


