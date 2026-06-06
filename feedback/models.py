from django.db import models
from user.models import User


class EmployeeQuery(models.Model):

    QUERY_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Rejected', 'Rejected'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    query_status = models.CharField(
        max_length=20,
        choices=QUERY_STATUS_CHOICES,
        default='Pending'
    )

    admin_reply = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.employee.name} - {self.subject}"


class EmployeeFeedback(models.Model):

    FEEDBACK_TYPE_CHOICES = [
        ('Work Environment', 'Work Environment'),
        ('Management', 'Management'),
        ('HR Policy', 'HR Policy'),
        ('Salary', 'Salary'),
        ('Leave', 'Leave'),
        ('Attendance', 'Attendance'),
        ('Other', 'Other'),
    ]

    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_type = models.CharField(max_length=100, choices=FEEDBACK_TYPE_CHOICES)
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    message = models.TextField()

    admin_note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.employee.name} - {self.feedback_type}"