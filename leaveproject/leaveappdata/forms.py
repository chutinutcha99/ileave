from django import forms
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


