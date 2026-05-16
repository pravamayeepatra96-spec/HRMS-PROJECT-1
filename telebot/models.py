from django.db import models
from user.models import User


class TelegramDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    empid = empid = models.CharField(max_length=20)
    #user_id = models.IntegerField()
    comp_code = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    chat_id = models.BigIntegerField(null=True, blank=True)
    telegram_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'telebot_telegramdetails'

    def __str__(self):
        return f'{self.empid} - {self.telegram_name}'
