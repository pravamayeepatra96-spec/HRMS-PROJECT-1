from django.shortcuts import render, redirect

from .models import Attendance

from datetime import date, datetime


def attendance_list(request):

    attendances = Attendance.objects.all()

    return render(
        request,
        'attendance_list.html',
        {'attendances': attendances}
    )


def attendance_details(request, id):

    attendance = Attendance.objects.get(id=id)

    return render(
        request,
        'attendance_details.html',
        {'attendance': attendance}
    )


def mark_attendance(request):

    if request.method == "POST":

        empid = request.POST.get('empid')

        Attendance.objects.create(

            empid=empid,

            date=date.today(),

            log_in_time=datetime.now().time(),

            log_out_time=datetime.now().time(),

            status=1
        )

        return redirect('/attendance-list/')

    return render(
        request,
        'mark_attendance.html'
    )
# Create your views here.
