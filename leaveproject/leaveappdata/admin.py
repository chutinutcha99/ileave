from django.contrib import admin
from .models import Leave_Form, Settings_Sort_Form

# Register your models here.
@admin.register(Leave_Form)

class Leave_FormAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'leave_type']

    def leave_type(self, obj):
        return obj.leave_sort_name.leave_sort_name

@admin.register(Settings_Sort_Form)

class Settings_Sort_FormAdmin(admin.ModelAdmin):
    pass