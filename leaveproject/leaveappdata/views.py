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
    leaveappdata_leave_form = Leave_Form.objects.all()
    print(leaveappdata_leave_form)
    return render(request, 'leaveappdata/showdata_approved.html', {'leaveform': leaveappdata_leave_form})

