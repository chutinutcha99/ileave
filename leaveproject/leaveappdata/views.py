from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LeaveForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'leaveappdata/home.html')

@login_required
def leave_form(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'บันทึกข้อมูลการลาเรียบร้อยแล้ว')
            return redirect('home')
    else:
        form = LeaveForm()
    return render(request, 'leaveappdata/leave_form.html', {'form': form})

