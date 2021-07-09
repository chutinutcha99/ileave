from django.contrib import admin
from .models import Leave_Form, Settings_Sort_Form

# Register your models here.
@admin.register(Leave_Form)

class Leave_FormAdmin(admin.ModelAdmin):
    pass

@admin.register(Settings_Sort_Form)

class Settings_Sort_FormAdmin(admin.ModelAdmin):
    pass