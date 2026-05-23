from django.shortcuts import render, redirect, get_object_or_404
from .models import Applicant
from .models import Applicant, JobOpening


def applicants_list(request):
    applicants = Applicant.objects.filter(status=1).order_by('-applied_date', '-id')

    return render(request, 'applicants_list.html', {
        'applicants': applicants
    })


def add_applicant(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        position_applied = request.POST.get('position_applied')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        application_status = request.POST.get('application_status')
        resume = request.FILES.get('resume')

        Applicant.objects.create(
            name=name,
            email=email,
            phone_no=phone_no,
            position_applied=position_applied,
            qualification=qualification,
            experience=experience,
            application_status=application_status,
            resume=resume,
            status=1
        )

        return redirect('applicants_list')

    return redirect('applicants_list')


def delete_applicant(request, applicant_id):
    applicant = get_object_or_404(Applicant, id=applicant_id)

    if request.method == "POST":
        applicant.status = 0
        applicant.save()

    return redirect('applicants_list')
def job_openings_list(request):
    jobs = JobOpening.objects.filter(status=1).order_by('-posted_date', '-id')

    return render(request, 'job_openings_list.html', {
        'jobs': jobs
    })


def add_job_opening(request):
    if request.method == "POST":
        title = request.POST.get('title')
        department = request.POST.get('department')
        location = request.POST.get('location')
        job_type = request.POST.get('job_type')
        experience_required = request.POST.get('experience_required')
        salary_range = request.POST.get('salary_range')
        description = request.POST.get('description')
        job_status = request.POST.get('job_status')

        JobOpening.objects.create(
            title=title,
            department=department,
            location=location,
            job_type=job_type,
            experience_required=experience_required,
            salary_range=salary_range,
            description=description,
            job_status=job_status,
            status=1
        )

        return redirect('job_openings_list')

    return redirect('job_openings_list')


def delete_job_opening(request, job_id):
    job = get_object_or_404(JobOpening, id=job_id)

    if request.method == "POST":
        job.status = 0
        job.save()

    return redirect('job_openings_list')