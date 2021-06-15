import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
SORT_NAME = (
    ('ลากิจส่วนตัว', 'ลากิจส่วนตัว'),
    ('ลาคลอดบุตร', 'ลาคลอดบุตร'),
    ('ลาป่วย', 'ลาป่วย'),
    ('ลาพักร้อน', 'ลาพักร้อน'),
    ('ลาเข้าตรวจรับเลือกทหารหรือเข้ารับการเตรียมพล', 'ลาเข้าตรวจรับเลือกทหารหรือเข้ารับการเตรียมพล'),
    ('ลาไปช่วยเหลือภรรยาที่คลอดบุตร', 'ลาไปช่วยเหลือภรรยาที่คลอดบุตร'),
    ('ลาไปศึกษา ฝึกอบรม ปฏิบัติการวิจัย หรือดูงาน', 'ลาไปศึกษา ฝึกอบรม ปฏิบัติการวิจัย หรือดูงาน'),
)

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

class Leave_Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_sort_name = models.CharField(max_length=200, choices=SORT_NAME, default='ลากิจส่วนตัว')
    leave_department = models.CharField(max_length=200, choices=DEPARTMENT_NAME, default='บริหาร')
    leave_reason = models.CharField(max_length=200)
    start_date = models.DateField(default=datetime.date.today)
    duration1 = models.CharField(max_length=100, choices=DURATION1, default='เต็มวัน')
    end_date = models.DateField(default=datetime.date.today)
    duration2 = models.CharField(max_length=100, choices=DURATION2, default='เต็มวัน')
    upload = models.FileField(upload_to='file_uploads')
    leave_contact = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = "leaveappdata_leave_form"
    
    def __str__(self):
        return self.leave_sort_name



    
