from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import House, Resident


class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'last_modified_date', 'start_date', 'end_date')


class ResidentAdmin(admin.ModelAdmin):
    list_display = ('user', 'house', 'type', 'status', 'last_modified_date', 'start_date', 'end_date')


# Register your models here.
admin.site.register(House, HouseAdmin)
admin.site.register(Resident, ResidentAdmin)
