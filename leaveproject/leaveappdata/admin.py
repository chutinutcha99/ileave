from django.contrib import admin
from .models import Leave_Form

# Register your models here.
@admin.register(Leave_Form)

class Leave_FormAdmin(admin.ModelAdmin):
    pass
