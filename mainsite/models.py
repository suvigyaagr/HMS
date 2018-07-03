import uuid
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date

class Job(models.Model):
    job_title = models.CharField(primary_key=True, max_length=100)

    def __str__ (self):
        return self.job_title


class Gender(models.Model):
    gender_title = models.CharField(primary_key=True, max_length=50)

    def __str__ (self):
        return self.gender_title


class AttendanceType(models.Model):
    attendance_value = models.FloatField(primary_key=True, validators=[MinValueValidator(0), MaxValueValidator(1.0)])
    attendance_value_name = models.CharField(max_length=100)

    def __str__ (self):
        return self.attendance_value_name


class Staff(models.Model):
    staff_name = models.CharField(max_length=200)
    staff_shortname = models.CharField(max_length=100)
    staff_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    staff_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    staff_doj = models.DateField(("Date"), default=date.today)
    staff_salary = models.PositiveIntegerField()
    staff_job_title = models.ForeignKey(Job, on_delete=models.PROTECT)
    staff_gender = models.ForeignKey(Gender, on_delete=models.PROTECT)

    def __str__(self):
        return self.staff_name + ' - ' + str(self.pk)

class StaffAttendance(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    attendance_date = models.DateField("Date")
    staff_attendance_value = models.ForeignKey(AttendanceType, on_delete=models.DO_NOTHING)

    def __str__ (self):
        return str(self.staff_id) + '-' + str(self.attendance_date) + '-' + str(self.staff_attendance_value)
