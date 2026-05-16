from django.db import models
from user.models import User

class Salary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    empid = models.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True)

    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.user and not self.role:
            self.role = self.user.role
        if self.user and not self.empid:
            self.empid = self.user.empid
        self.net_salary = self.basic_salary + self.bonuses - self.deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.empid or self.user.empid if self.user else 'Unknown'} - {self.net_salary}"
