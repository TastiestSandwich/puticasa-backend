from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'last_modified_date', 'start_date', 'end_date')


# Register your models here.
admin.site.register(House, HouseAdmin)
