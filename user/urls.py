from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),

    path('add-employee-page/', views.add_employee_page, name='add_employee_page'),

    path('profile-details/', views.profile_details, name='profile_details'),
    path('employee-profile/<int:employee_id>/', views.employee_profile_details, name='employee_profile_details'),

    path('add_employee/', views.add_employee, name='add_employee'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    path('logout/', views.logout, name='logout'),
]