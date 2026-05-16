from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    owner_id = models.CharField(max_length=10)
    code = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name
class User(models.Model):

    ROLE_CHOICES = [
        ('HR', 'HR'),
        ('Employee', 'Employee'),
        ('Manager', 'Manager'),
        ('Team Lead', 'Team Lead'),
        ('Intern', 'Intern'),
        ('Admin', 'Admin'),
    ]

    Company = models.ForeignKey(Company, on_delete=models.CASCADE)

    empid = models.CharField(max_length=10, unique=True)

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)

    password = models.CharField(max_length=100)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    joining_date = models.DateField()
    exit_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
    
    
# Create your models here.
