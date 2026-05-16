from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404

from user.models import User
from .models import Salary


def salary_list(request):
    salaries = Salary.objects.select_related('user').all().order_by('user__name')
    users = User.objects.filter(status=1).order_by('name')
    return render(
        request,
        'salary_list.html',
        {
            'salaries': salaries,
            'users': users,
        }
    )


def salary_create(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        basic_salary = Decimal(request.POST.get('basic_salary', '0'))
        bonuses = Decimal(request.POST.get('bonuses', '0'))
        deductions = Decimal(request.POST.get('deductions', '0'))

        user = get_object_or_404(User, id=user_id)
        salary, created = Salary.objects.get_or_create(
            user=user,
            defaults={
                'empid': user.empid,
                'role': user.role,
                'basic_salary': basic_salary,
                'bonuses': bonuses,
                'deductions': deductions,
            }
        )

        if not created:
            salary.basic_salary = basic_salary
            salary.bonuses = bonuses
            salary.deductions = deductions
            salary.save()

        return redirect('salary_list')

    return redirect('salary_list')


def salary_update(request, id):
    salary = get_object_or_404(Salary, id=id)
    if request.method == "POST":
        salary.basic_salary = Decimal(request.POST.get('basic_salary', salary.basic_salary))
        salary.bonuses = Decimal(request.POST.get('bonuses', salary.bonuses))
        salary.deductions = Decimal(request.POST.get('deductions', salary.deductions))
        salary.save()
        return redirect('salary_list')

    return redirect('salary_list')


def salary_delete(request, id):
    salary = get_object_or_404(Salary, id=id)
    if request.method == 'POST':
        salary.delete()
    return redirect('salary_list')


def salary_details(request, id):
    salary = Salary.objects.get(id=id)
    return render(
        request,
        'salary_details.html',
        {'salary': salary}
    )


def check_salary(request):
    if request.method == "POST":
        empid = request.POST.get('empid')
        try:
            salary = Salary.objects.get(empid=empid)
            return render(
                request,
                'check_salary.html',
                {'salary': salary}
            )
        except Salary.DoesNotExist:
            return render(
                request,
                'check_salary.html',
                {'error': 'Salary Record Not Found'}
            )
    return render(
        request,
        'check_salary.html'
    )