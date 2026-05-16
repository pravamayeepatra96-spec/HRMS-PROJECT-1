from django.urls import path

from .views import (
    telegram_list,
    telegram_details,
    telegram_profile
)

urlpatterns = [

    path('telegram-list/', telegram_list),

    path('telegram-details/<int:id>/', telegram_details),

    path('telegram-profile/', telegram_profile),

]