import datetime
from django.db import models
from django.contrib.auth.models import User
import numpy as np


# Create your models here.

# Settings_Sort_Form 
class Settings_Sort_Form(models.Model):
    leave_sort_name = models.CharField(max_length=200, default='')
    leave_days = models.CharField(max_length=3)

    class Meta:
        db_table = "leaveappdata_settings_sort_form"

    def __str__(self):
        return self.leave_sort_name


'''SORT_NAME = (
    ('ลากิจส่วนตัว', 'ลากิจส่วนตัว'),
    ('ลาคลอดบุตร', 'ลาคลอดบุตร'),
    ('ลาป่วย', 'ลาป่วย'),
    ('ลาพักร้อน', 'ลาพักร้อน'),
    ('ลาเข้าตรวจรับเลือกทหารหรือเข้ารับการเตรียมพล', 'ลาเข้าตรวจรับเลือกทหารหรือเข้ารับการเตรียมพล'),
    ('ลาไปช่วยเหลือภรรยาที่คลอดบุตร', 'ลาไปช่วยเหลือภรรยาที่คลอดบุตร'),
    ('ลาไปศึกษา ฝึกอบรม ปฏิบัติการวิจัย หรือดูงาน', 'ลาไปศึกษา ฝึกอบรม ปฏิบัติการวิจัย หรือดูงาน'),
)'''

DEPARTMENT_NAME = (
    ('บริหาร', 'บริหาร'),
    ('จัดซื้อจัดจ้าง', 'จัดซื้อจัดจ้าง'),
    ('บุคคล', 'บุคคล'),
)

DURATION1 = ( 
    ('เต็มวัน', 'เต็มวัน'),
    ('ครึ่งเช้า', 'ครึ่งเช้า'),
    ('ครึ่งบ่าย', 'ครึ่งบ่าย'),
)

DURATION2 = (
    ('เต็มวัน', 'เต็มวัน'),
    ('ครึ่งเช้า', 'ครึ่งเช้า'),
    ('ครึ่งบ่าย', 'ครึ่งบ่าย'),
)

STATUSES_CHOICES = (
    ('รออนุมัติ', 'รออนุมัติ'),
    ('อนุมัติ', 'อนุมัติ'),
    ('ไม่อนุมัติ', 'ไม่อนุมัติ'),
)


class Leave_Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_sort_name = models.ForeignKey(Settings_Sort_Form, on_delete=models.CASCADE)
    leave_department = models.CharField(max_length=200, choices=DEPARTMENT_NAME, default='บริหาร')
    leave_reason = models.CharField(max_length=200)
    start_date = models.DateField(default=datetime.date.today)
    duration1 = models.CharField(max_length=100, choices=DURATION1, default='เต็มวัน')
    end_date = models.DateField(default=datetime.date.today)
    duration2 = models.CharField(max_length=100, choices=DURATION2, default='เต็มวัน')
    upload = models.FileField(upload_to='file_uploads')
    leave_contact = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=STATUSES_CHOICES, default='รออนุมัติ')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    '''def status_update(self):
        self.status = 'รออนุมัติ'
        self.save()'''


    def days_leave(self):
        start_date = self.start_date
        end_date = self.end_date

        return np.busday_count(start_date, end_date) + 1

    class Meta:
        db_table = "leaveappdata_leave_form"
    
    def __str__(self):
        return self.leave_sort_name



    

    
