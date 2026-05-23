from django.urls import path
from . import views

urlpatterns = [
    path('reports/employees/', views.employee_reports, name='employee_reports'),
    path('reports/attendance/', views.attendance_reports, name='attendance_reports'),
    path('reports/salary/', views.salary_reports, name='salary_reports'),
]