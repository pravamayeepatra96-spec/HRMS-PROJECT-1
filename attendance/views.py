from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, datetime

from .models import Attendance


def attendance_list(request):
    attendances = Attendance.objects.all().order_by('-date', '-id')

    return render(
        request,
        'attendance_list.html',
        {
            'attendances': attendances
        }
    )


def attendance_details(request, id):
    attendance = get_object_or_404(Attendance, id=id)

    return render(
        request,
        'attendance_details.html',
        {
            'attendance': attendance
        }
    )


def mark_attendance(request):
    if request.method == "POST":
        empid = request.POST.get('empid')

        if empid:
            Attendance.objects.create(
                empid=empid,
                date=date.today(),
                log_in_time=datetime.now().time(),
                log_out_time=datetime.now().time(),
                status=1
            )

        return redirect('attendance_list')

    return render(
        request,
        'mark_attendance.html'
    )