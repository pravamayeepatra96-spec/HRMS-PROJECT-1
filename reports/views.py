from django.shortcuts import render


def employee_reports(request):
    return render(request, 'employee_reports.html')


def attendance_reports(request):
    return render(request, 'attendance_reports.html')


def salary_reports(request):
    return render(request, 'salary_reports.html')