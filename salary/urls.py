from django.urls import path

from .views import (
    salary_list,
    salary_create,
    salary_update,
    salary_delete,
    salary_details,
    check_salary
)

urlpatterns = [
    path('salary-list/', salary_list, name='salary_list'),
    path('salary-create/', salary_create, name='salary_create'),
    path('salary-update/<int:id>/', salary_update, name='salary_update'),
    path('salary-delete/<int:id>/', salary_delete, name='salary_delete'),
    path('salary-details/<int:id>/', salary_details, name='salary_details'),
    path('check-salary/', check_salary, name='check_salary'),
]