import numpy as np
import datetime as dt

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LeaveForm
from leaveappdata.models import Leave_Form

# Create your views here.
@login_required
def home(request):
    return render(request, 'leaveappdata/home.html')

@login_required
def leave_form(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST, request.FILES)
        if form.is_valid():
            leaveappdata = form.save(commit=False)
            leaveappdata.user = request.user
            leaveappdata.save()
            messages.success(request, f'บันทึกข้อมูลการลาเรียบร้อยแล้ว')
            return redirect('leave_form')
        else:
            print('Error :', form.errors)
    else:
        form = LeaveForm()
    return render(request, 'leaveappdata/leave_form.html', {'form': form})

@login_required
def showdata_approved(request):
    showdata = Leave_Form.objects.all()
    for dt in showdata:
        if dt.user_id == request.user.username:
            start_date = dt.date(2021, 1, 1)
            end_date = dt.date(2021, 12, 31)

            days = np.busday_count(start_date, end_date)

            print(days)

    context = {'showdata': showdata}

    return render(request, 'leaveappdata/showdata_approved.html', days, context)
