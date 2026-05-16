from django.db import models
from django.utils import timezone
from user.models import User


class LeavePolicy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    paid_leave = models.IntegerField(default=0)
    casual_leave = models.IntegerField(default=0)
    sick_leave = models.IntegerField(default=0)
    compensation_leave = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        total = (
    int(self.paid_leave) +
    int(self.casual_leave) +
    int(self.sick_leave) +
    int(self.compensation_leave)
)

        LeaveBalance.objects.update_or_create(
            user=self.user,
            defaults={
                "paid_leave": self.paid_leave,
                "casual_leave": self.casual_leave,
                "sick_leave": self.sick_leave,
                "compensation_leave": self.compensation_leave,
                "total_leaves": total,
                "used_leaves": 0,
                "remaining_leaves": total,
                "year": timezone.now().year,
                "status": 1,
            }
        )

    def __str__(self):
        return f"{self.user.name} - Policy"


class ApplyLeave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    type_of_leave = models.CharField(max_length=50)
    reason_of_leave = models.TextField()

    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.name} - {self.type_of_leave}"


class LeaveBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    paid_leave = models.IntegerField(default=0)
    casual_leave = models.IntegerField(default=0)
    sick_leave = models.IntegerField(default=0)
    compensation_leave = models.IntegerField(default=0)

    total_leaves = models.IntegerField(default=0)
    used_leaves = models.IntegerField(default=0)
    remaining_leaves = models.IntegerField(default=0)
    year = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.name} - {self.remaining_leaves}"