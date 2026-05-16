from django.urls import path

from .views import (
    attendance_list,
    attendance_details,
    mark_attendance
)

urlpatterns = [

    path('attendance-list/', attendance_list),

    path('attendance-details/<int:id>/', attendance_details),

    path('mark-attendance/', mark_attendance),

]