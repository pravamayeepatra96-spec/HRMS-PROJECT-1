from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeQuery, EmployeeFeedback
from user.models import User


# =========================
# EMPLOYEE QUERY VIEWS
# =========================

def queries_list(request):
    queries = EmployeeQuery.objects.filter(status=1).order_by('-created_at')

    return render(request, 'queries_list.html', {
        'queries': queries
    })


def add_query(request):
    employees = User.objects.filter(status=1).order_by('empid')

    if request.method == "POST":
        employee_id = request.POST.get('employee')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        priority = request.POST.get('priority')

        employee = get_object_or_404(User, id=employee_id)

        EmployeeQuery.objects.create(
            employee=employee,
            subject=subject,
            message=message,
            priority=priority,
            query_status='Pending'
        )

        return redirect('queries_list')

    return render(request, 'add_query.html', {
        'employees': employees
    })


def reply_query(request, id):
    query = get_object_or_404(EmployeeQuery, id=id, status=1)

    if request.method == "POST":
        query.query_status = request.POST.get('query_status')
        query.admin_reply = request.POST.get('admin_reply')
        query.save()

        return redirect('queries_list')

    return render(request, 'reply_query.html', {
        'query': query
    })


def delete_query(request, id):
    query = get_object_or_404(EmployeeQuery, id=id, status=1)
    query.status = 0
    query.save()

    return redirect('queries_list')


# =========================
# EMPLOYEE FEEDBACK VIEWS
# =========================

def feedback_list(request):
    feedbacks = EmployeeFeedback.objects.filter(status=1).order_by('-created_at')

    return render(request, 'feedback_list.html', {
        'feedbacks': feedbacks
    })


def add_feedback(request):
    employees = User.objects.filter(status=1).order_by('empid')

    if request.method == "POST":
        employee_id = request.POST.get('employee')
        feedback_type = request.POST.get('feedback_type')
        rating = request.POST.get('rating')
        message = request.POST.get('message')

        employee = get_object_or_404(User, id=employee_id)

        EmployeeFeedback.objects.create(
            employee=employee,
            feedback_type=feedback_type,
            rating=rating,
            message=message
        )

        return redirect('feedback_list')

    return render(request, 'add_feedback.html', {
        'employees': employees
    })


def add_feedback_note(request, id):
    feedback = get_object_or_404(EmployeeFeedback, id=id, status=1)

    if request.method == "POST":
        feedback.admin_note = request.POST.get('admin_note')
        feedback.save()

        return redirect('feedback_list')

    return render(request, 'add_feedback_note.html', {
        'feedback': feedback
    })


def delete_feedback(request, id):
    feedback = get_object_or_404(EmployeeFeedback, id=id, status=1)
    feedback.status = 0
    feedback.save()

    return redirect('feedback_list')