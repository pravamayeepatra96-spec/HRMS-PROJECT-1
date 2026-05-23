from django.shortcuts import render, redirect

from user.models import User
from .models import (
    LeavePolicy,
    ApplyLeave,
    LeaveBalance
)


def leave_policy(request):
    company_id = request.session.get('company_id')

    if company_id:
        users = User.objects.filter(Company_id=company_id).order_by('name')
    else:
        users = User.objects.all().order_by('name')

    employee_policies = []

    for user in users:
        policy = LeavePolicy.objects.filter(user=user, status=1).first()

        employee_policies.append({
            'employee': user,
            'policy': policy
        })

    return render(
        request,
        'leave_policy.html',
        {
            'employee_policies': employee_policies
        }
    )


def apply_leave(request):

    if request.method == "POST":

        empid = request.POST.get('empid')

        user = User.objects.get(empid=empid)

        from_date = request.POST.get('from_date')

        to_date = request.POST.get('to_date')

        type_of_leave = request.POST.get('type_of_leave')

        reason_of_leave = request.POST.get('reason_of_leave')

        ApplyLeave.objects.create(
            user=user,
            from_date=from_date,
            to_date=to_date,
            type_of_leave=type_of_leave,
            reason_of_leave=reason_of_leave,
            approved=False,
            rejected=False,
            status=1
        )

        return redirect('leave_balance')

    return render(
        request,
        'apply_leave.html'
    )


def leave_balance(request):
    company_id = request.session.get('company_id')

    if company_id:
        balances = LeaveBalance.objects.filter(
            user__Company_id=company_id,
            status=1
        ).select_related('user').order_by('user__name')
    else:
        balances = LeaveBalance.objects.filter(
            status=1
        ).select_related('user').order_by('user__name')

    return render(
        request,
        'leave_balance.html',
        {
            'balances': balances
        }
    )


def update_leave_policy(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)

        policy, created = LeavePolicy.objects.get_or_create(
            user=user,
            defaults={
                'status': 1
            }
        )

        policy.paid_leave = request.POST.get('paid_leave', policy.paid_leave)
        policy.casual_leave = request.POST.get('casual_leave', policy.casual_leave)
        policy.sick_leave = request.POST.get('sick_leave', policy.sick_leave)
        policy.compensation_leave = request.POST.get('compensation_leave', policy.compensation_leave)

        policy.save()

        return redirect('leave_policy')

    return redirect('leave_policy')