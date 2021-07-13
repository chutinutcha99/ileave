from django.urls import path
from . import views

urlpatterns = [
    
    path('leave_form/',views.leave_form, name='leave_form'),
    path('showdata_pending/',views.showdata_pending, name='showdata_pending'),
    path('showdata_approved/',views.showdata_approved, name='showdata_approved'),
    path('showdata_rejected/',views.showdata_rejected, name='showdata_rejected'),
    path('approve_leave_form/<int:id>/<int:approve>/',views.approve_leave_form, name='approve_leave_form'),
    path('list_leave/',views.list_leave, name='list_leave'),
    path('settings_sort_list/',views.settings_sort_list, name='settings_sort_list'),
    path('settings_sort_form/',views.settings_sort_form, name='settings_sort_form'),
    path('delete_sort/<int:id>/',views.deleteSort, name='delete_sort'),
]

