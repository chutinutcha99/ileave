import datetime
from django import forms
from django.db.models import fields
from .models import Leave_Form, Settings_Sort_Form, DEPARTMENT_NAME, DURATION1, DURATION2

class LeaveForm(forms.ModelForm):

    class Meta: 

        model = Leave_Form

        fields = '__all__'

        exclude = ('user', 'updated', 'created', 'status',)

class SettingsSortForm(forms.ModelForm):

    class Meta:

        model = Settings_Sort_Form

        fields = '__all__'

        exclude = ('user',)

class SettingsSortEdit(forms.ModelForm):

    class Meta: 

        model = Settings_Sort_Form
        
        fields =('leave_sort_name', 'leave_days',)


