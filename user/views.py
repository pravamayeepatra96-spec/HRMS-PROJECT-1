from .forms import SignupForm, LoginForm
from .models import User, Company

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import models
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json


def login(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(
                    email=email,
                    password=password
                )

                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['user_role'] = user.role
                request.session['company_id'] = user.Company.id
                request.session['company_name'] = user.Company.name

                return redirect('dashboard')

            except User.DoesNotExist:

                return render(
                    request,
                    'login.html',
                    {
                        'form': form,
                        'error': 'Invalid Email or Password'
                    }
                )

    else:
        form = LoginForm()

    return render(
        request,
        'login.html',
        {'form': form}
    )


def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            try:
                company_name = form.cleaned_data['company_name']
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                if password != confirm_password:
                    messages.error(request, 'Passwords do not match.')
                    return render(request, 'signup.html', {'form': form})

                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already registered. Please login.')
                    return render(request, 'signup.html', {'form': form})

                if Company.objects.filter(name=company_name).exists():
                    messages.error(request, 'Company already exists. Please contact admin.')
                    return render(request, 'signup.html', {'form': form})

                company = Company.objects.create(
                    name=company_name,
                    owner_id='',
                    code=''
                )

                company.code = "CMP00" + str(company.id)
                company.save()

                user = User.objects.create(
                    Company=company,
                    empid='',
                    name=name,
                    email=email,
                    phone_no=phone,
                    password=password,
                    role='Admin',
                    joining_date=timezone.now().date()
                )

                user.empid = "EMP00" + str(user.id)
                user.save()

                company.owner_id = user.empid
                company.save()

                messages.success(request, 'Account created successfully. Please login.')
                return redirect('login')

            except Exception as e:
                messages.error(request, f'Error creating account: {str(e)}')
                return render(request, 'signup.html', {'form': form})

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def dashboard(request):

    if 'user_id' not in request.session:
        return redirect('login')

    company_id = request.session['company_id']

    employees = User.objects.filter(Company_id=company_id)

    total_employees = employees.count()
    total_admins = employees.filter(role='Admin').count()
    total_hr = employees.filter(role='HR').count()
    total_managers = employees.filter(role='Manager').count()
    total_team_leads = employees.filter(role='Team Lead').count()
    total_interns = employees.filter(role='Intern').count()

    recent_employees = employees.order_by('-created_at')[:5]

    context = {
        'total_employees': total_employees,
        'total_admins': total_admins,
        'total_hr': total_hr,
        'total_managers': total_managers,
        'total_team_leads': total_team_leads,
        'total_interns': total_interns,
        'recent_employees': recent_employees,

        'user_name': request.session['user_name'],
        'user_role': request.session['user_role'],
        'company_name': request.session['company_name'],
    }

    return render(request, 'admin_dashboard.html', context)


def employee_list(request):

    if 'user_id' not in request.session:
        return redirect('login')

    company_id = request.session['company_id']

    employees = User.objects.filter(
        Company_id=company_id
    ).order_by('-created_at')

    context = {
        'employees': employees,
        'user_name': request.session['user_name'],
        'user_role': request.session['user_role'],
        'company_name': request.session['company_name'],
    }

    return render(request, 'dashboard.html', context)


@csrf_exempt
def add_employee(request):

    if 'user_id' not in request.session:
        return JsonResponse({'success': False, 'message': 'Not logged in'})

    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            company_id = request.session['company_id']

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Email already exists'
                })

            company = Company.objects.get(id=company_id)

            max_id = User.objects.filter(
                Company=company
            ).aggregate(
                max_id=models.Max('id')
            )['max_id'] or 0

            empid = f"EMP{str(max_id + 1).zfill(3)}"

            employee = User.objects.create(
                Company=company,
                empid=empid,
                name=data['name'],
                email=data['email'],
                phone_no=data['phone'],
                password=data['password'],
                role=data['role'],
                joining_date=data['joining_date']
            )

            return JsonResponse({
                'success': True,
                'message': 'Employee added successfully',
                'employee': {
                    'id': employee.id,
                    'empid': employee.empid,
                    'name': employee.name,
                    'email': employee.email,
                    'phone_no': employee.phone_no,
                    'role': employee.role,
                    'joining_date': employee.joining_date.strftime('%Y-%m-%d')
                }
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })

    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    })


@csrf_exempt
def update_employee(request, employee_id):

    if 'user_id' not in request.session:
        return JsonResponse({'success': False, 'message': 'Not logged in'})

    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            company_id = request.session['company_id']

            employee = get_object_or_404(
                User,
                id=employee_id,
                Company_id=company_id
            )

            if data['email'] != employee.email and User.objects.filter(email=data['email']).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Email already exists'
                })

            employee.name = data['name']
            employee.email = data['email']
            employee.phone_no = data['phone']
            employee.role = data['role']
            employee.joining_date = data['joining_date']

            if 'password' in data and data['password']:
                employee.password = data['password']

            employee.save()

            return JsonResponse({
                'success': True,
                'message': 'Employee updated successfully',
                'employee': {
                    'id': employee.id,
                    'empid': employee.empid,
                    'name': employee.name,
                    'email': employee.email,
                    'phone_no': employee.phone_no,
                    'role': employee.role,
                    'joining_date': employee.joining_date.strftime('%Y-%m-%d')
                }
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })

    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    })


@csrf_exempt
def delete_employee(request, employee_id):

    if 'user_id' not in request.session:
        return JsonResponse({'success': False, 'message': 'Not logged in'})

    if request.method == 'POST':

        try:
            company_id = request.session['company_id']

            employee = get_object_or_404(
                User,
                id=employee_id,
                Company_id=company_id
            )

            if employee.role == 'Admin':
                return JsonResponse({
                    'success': False,
                    'message': 'Cannot delete admin user'
                })

            employee.delete()

            return JsonResponse({
                'success': True,
                'message': 'Employee deleted successfully'
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })

    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    })

git a
def logout(request):

    request.session.flush()

    return redirect('login')