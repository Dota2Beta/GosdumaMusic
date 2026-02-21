from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Application, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Дополнительно", {"fields": ("full_name", "phone")}),)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'event_date', 'genre', 'participation_format', 'status', 'created_at')
    list_filter = ('status', 'participation_format', 'event_date')
    search_fields = ('title', 'genre', 'user__username')
