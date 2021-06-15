import datetime
from django import forms
from .models import Leave_Form, SORT_NAME, DEPARTMENT_NAME, DURATION1, DURATION2

class LeaveForm(forms.ModelForm):
    leave_sort_name = forms.ChoiceField(choices=SORT_NAME, widget=forms.Select, initial='--')
    leave_department = forms.ChoiceField(choices=DEPARTMENT_NAME, widget=forms.Select, initial='--')
    leave_reason = forms.CharField(widget=forms.Textarea)
    '''start_date = forms.DateField(widget=DateInput(format='%Y/%m/%d'), input_formats=('%Y/%m/%d',))'''
    start_date = forms.DateField()
    duration1 = forms.ChoiceField(choices=DURATION1, widget=forms.Select, initial='--')
    '''end_date = forms.DateField(widget=DateInput(format='%Y/%m/%d'), input_formats=('%Y/%m/%d',))'''
    end_date = forms.DateField()
    duration2 = forms.ChoiceField(choices=DURATION2, widget=forms.Select, initial='--')
    leave_contact = forms.CharField(widget=forms.Textarea)
    updated = forms.DateField()
    created = forms.DateField()

    class Meta: 

        model = Leave_Form

        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
        }

