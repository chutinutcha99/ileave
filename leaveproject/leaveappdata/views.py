from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LeaveForm, SettingsSortForm, SettingsDepartmentForm
from leaveappdata.models import Leave_Form, Settings_Sort_Form, Settings_Department_Form
from django.db.models import Q, Sum, Count, F, Max

# Create your views here.
@login_required
def home(request):
    members = User.objects.count()
    pending_count = Leave_Form.objects.filter(status='รออนุมัติ').count()
    approve_count = Leave_Form.objects.filter(status='อนุมัติ').count()
    rejects_count = Leave_Form.objects.filter(status='ไม่อนุมัติ').count()

    context = {
        'members': members,
        'pending_count': pending_count,
        'approve_count': approve_count,
        'rejects_count': rejects_count
        
        }
    return render(request, 'leaveappdata/home.html', context)


def ChangeActions(user):
    if user.groups.filter(Q(name = 'HR') | Q(name = 'Supervisor')).exists():
        return True
    return False
        

@login_required
def leave_form(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST, request.FILES)
        if form.is_valid():
            leaveappdata = form.save(commit=False)
            leaveappdata.user = request.user
            leaveappdata.save()
            #messages.success(request, f'บันทึกข้อมูลการลาเรียบร้อยแล้ว')
            return redirect('leaveappdata:list_leave')
        else:
            print('Error :', form.errors)
    else:
        form = LeaveForm()
    return render(request, 'leaveappdata/leave_form.html', {'form': form})

@login_required
def showdata_pending(request):
    showdata_p = Leave_Form.objects.filter(status='รออนุมัติ')
    
    
    context = {'showdata_p': showdata_p}
    return render(request, 'leaveappdata/showdata_pending.html', context)

@login_required
def showdata_approved(request):
    showdata_a = Leave_Form.objects.filter(status='อนุมัติ')

    context = {'showdata_a': showdata_a}
    return render(request, 'leaveappdata/showdata_approved.html', context)

@login_required
def showdata_rejected(request):
    showdata_r = Leave_Form.objects.filter(status='ไม่อนุมัติ')

    context = {'showdata_r': showdata_r}
    return render(request, 'leaveappdata/showdata_rejected.html', context)

@login_required
def approve_leave_form(request, id, approve = 1):
    approve_leave = Leave_Form.objects.get(id = id)
    print(approve_leave)
    if approve == 0:
        approve_leave.status = 'ไม่อนุมัติ'
        approve_leave.save()
        return redirect('/leaveappdata/showdata_rejected/')
    elif approve == 1:
        approve_leave.status = 'อนุมัติ'
        approve_leave.save()
        return redirect('/leaveappdata/showdata_approved/')
    

@login_required
@user_passes_test(ChangeActions, login_url='/')
def list_leave(request):
    approve_leave = Leave_Form.objects.filter(status='รออนุมัติ')

    context = {'approve_leave': approve_leave}
    return render(request, 'leaveappdata/list_leave.html', context)


@login_required
def showdata_rejected(request):
    showdata_r = Leave_Form.objects.filter(status='ไม่อนุมัติ')

    context = {'showdata_r': showdata_r}
    return render(request, 'leaveappdata/showdata_rejected.html', context)

@login_required
def settings_sort_form(request):
    if request.method == 'POST':
        form = SettingsSortForm(request.POST)
        if form.is_valid():
            leaveappdata = form.save(commit=False)
            leaveappdata.user = request.user
            leaveappdata.save()
            return redirect('leaveappdata:settings_sort_list')
        else:
            print('Error :', form.errors)
    else:
        form = SettingsSortForm()
    return render(request, 'leaveappdata/settings_sort_form.html', {'form':form})

@login_required
def settings_sort_list(request):
    sort_list = Settings_Sort_Form.objects.all()

    context = {'sort_list': sort_list}
    return render(request, 'leaveappdata/settings_sort_list.html', context)

@login_required
def deleteSort(request, id):
        delete_sort = Settings_Sort_Form.objects.get(id = id)
        print(delete_sort)
        if request.method == 'POST':

            delete_sort.delete()
            return redirect('leaveappdata:settings_sort_list')
        
        return render(request, 'leaveappdata/delete_sort.html')


@login_required
def settings_department_form(request):
    if request.method == 'POST':
        form = SettingsDepartmentForm(request.POST)
        if form.is_valid():
            leaveappdata = form.save(commit=False)
            leaveappdata.user = request.user
            leaveappdata.save()
            return redirect('leaveappdata:settings_department_list')
        else:
            print('Error :', form.errors)
    else:
        form = SettingsDepartmentForm()
    return render(request, 'leaveappdata/settings_department_form.html', {'form':form})

@login_required
def settings_department_list(request):
    department_list = Settings_Department_Form.objects.all()

    context = {'department_list': department_list}
    return render(request, 'leaveappdata/settings_department_list.html', context)

@login_required
def deleteDepartment(request, id):
        delete_department = Settings_Department_Form.objects.get(id = id)
        print(delete_department)
        if request.method == 'POST':

            delete_department.delete()
            return redirect('leaveappdata:settings_department_list')
        
        return render(request, 'leaveappdata/delete_department.html')


'''def settings_sort_edit(request, id=None):
    sort_edit = Settings_Sort_Form.objects.get(id = id)
    if request.method == 'POST':
        form = SettingsSortEdit(request.POST, instance=sort_edit)
        if form.is_valid():
            form.save()
            messages.success(request, f'ประเภทการลาแก้ไขเรียบร้อยแล้ว')
            return redirect('settings_sort_list')
        else:
            print('Error :', form.errors)
    else:
        form = SettingsSortEdit(instance=sort_edit)
    return render(request, 'leaveappdata/settings_sort_edit.html', {'form': form})'''

def statistics(request):
    result = Leave_Form.objects.annotate(
                                    LeaveType=F('leave_sort_name__leave_sort_name')
                                ).values(
                                    'user',
                                    'LeaveType' 
                                ).annotate(
                                    LeaveDay = Sum('numdays'),
                                    MaxLeaveDay = Max('leave_sort_name__leave_days')
                                ).annotate(RemainingLeaveDays = 
                                    F('MaxLeaveDay') - F('LeaveDay')
                                )
                                
    context = {'result': result}                           
    return render(request, 'leaveappdata/statistics.html', context)


