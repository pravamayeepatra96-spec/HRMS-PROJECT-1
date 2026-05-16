from django.urls import path

from .views import (
    leave_policy,
    apply_leave,
    leave_balance,
    update_leave_policy
)

urlpatterns = [

    path('leave-policy/', leave_policy, name='leave_policy'),

    path('apply-leave/', apply_leave, name='apply_leave'),

    path('leave-balance/', leave_balance, name='leave_balance'),

    path('update-leave-policy/<int:user_id>/', update_leave_policy, name='update_leave_policy'),

]