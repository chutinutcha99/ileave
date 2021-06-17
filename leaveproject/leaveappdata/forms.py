import datetime
from django import forms
from .models import Leave_Form, SORT_NAME, DEPARTMENT_NAME, DURATION1, DURATION2

class LeaveForm(forms.ModelForm):

    class Meta: 

        model = Leave_Form

        fields = '__all__'

        exclude = ('user', 'updated', 'created',)

