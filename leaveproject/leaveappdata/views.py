from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import LeaveForm, SettingsSortForm
from leaveappdata.models import Leave_Form, Settings_Sort_Form
from django.db.models import Q

# Create your views here.
@login_required
def home(request):
    return render(request, 'leaveappdata/home.html')

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
            messages.success(request, f'บันทึกข้อมูลการลาเรียบร้อยแล้ว')
            return redirect('leave_form')
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
def approve_leave_form(id, approve = 1):
    approve_leave = Leave_Form.objects.get(id = id)
    print(approve_leave)
    if approve == 0:
        approve_leave.status = 'ไม่อนุมัติ'
        approve_leave.save()
        return redirect('/showdata_rejected/')
    elif approve == 1:
        approve_leave.status = 'อนุมัติ'
        approve_leave.save()
        return redirect('/showdata_approved/')
    

@login_required
@user_passes_test(ChangeActions, login_url='/')
def list_leave(request):
    approve_leave = Leave_Form.objects.filter(status='รออนุมัติ')

    context = {'approve_leave': approve_leave}
    return render(request, 'leaveappdata/list_leave.html', context)


def showdata_rejected(request):
    showdata_r = Leave_Form.objects.filter(status='ไม่อนุมัติ')

    context = {'showdata_r': showdata_r}
    return render(request, 'leaveappdata/showdata_rejected.html', context)


def settings_sort_form(request):
    if request.method == 'POST':
        form = SettingsSortForm(request.POST)
        if form.is_valid():
            leaveappdata = form.save(commit=False)
            leaveappdata.user = request.user
            leaveappdata.save()
            messages.success(request, f'บันทึกประเภทการลาเรียบร้อยแล้ว')
            return redirect('settings_sort_form')
        else:
            print('Error :', form.errors)
    else:
        form = SettingsSortForm()
    return render(request, 'leaveappdata/settings_sort_form.html', {'form':form})


def settings_sort_list(request):
    sort_list = Settings_Sort_Form.objects.all()

    context = {'sort_list': sort_list}
    return render(request, 'leaveappdata/settings_sort_list.html', context)

def deleteSort(request, id):
        #delete_sort = get_object_or_404(Settings_Sort_Form, id = id)
        delete_sort = Settings_Sort_Form.objects.get(id = id)
        print(delete_sort)
        if request.method == 'POST':

            delete_sort.delete()
            return redirect('setting_sort_list')

        context = {'delete_sort': delete_sort}
        return render(request, 'leaveappdata/delete_sort.html', context)


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

