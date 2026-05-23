from django.db import models
from user.models import User

class EmployeeDocument(models.Model):

    DOCUMENT_TYPE_CHOICES = [
        ('Aadhaar Card', 'Aadhaar Card'),
        ('PAN Card', 'PAN Card'),
        ('Resume', 'Resume'),
        ('Offer Letter', 'Offer Letter'),
        ('Joining Letter', 'Joining Letter'),
        ('Experience Certificate', 'Experience Certificate'),
        ('Educational Certificate', 'Educational Certificate'),
        ('Salary Slip', 'Salary Slip'),
        ('ID Proof', 'ID Proof'),
        ('Other', 'Other'),
    ]

    VERIFICATION_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPE_CHOICES)
    document_file = models.FileField(upload_to='employee_documents/')
    uploaded_date = models.DateTimeField(auto_now_add=True)

    verification_status = models.CharField(
        max_length=20,
        choices=VERIFICATION_STATUS_CHOICES,
        default='Pending'
    )

    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.employee.name} - {self.document_type}"