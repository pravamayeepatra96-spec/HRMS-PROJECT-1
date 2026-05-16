from django.db import models

class Attendance(models.Model):
    empid = models.CharField(max_length=20)
    date = models.DateField()
    log_in_time = models.TimeField()
    log_out_time = models.TimeField(null=True, blank=True)
    status = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.empid)
# Create your models here.
