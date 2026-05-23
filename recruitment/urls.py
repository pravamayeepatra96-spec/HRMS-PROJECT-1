from django.urls import path
from .views import (
    applicants_list,
    add_applicant,
    delete_applicant,
    job_openings_list,
    add_job_opening,
    delete_job_opening
)

urlpatterns = [
    path('applicants/', applicants_list, name='applicants_list'),
    path('add-applicant/', add_applicant, name='add_applicant'),
    path('delete-applicant/<int:applicant_id>/', delete_applicant, name='delete_applicant'),

    path('job-openings/', job_openings_list, name='job_openings_list'),
    path('add-job-opening/', add_job_opening, name='add_job_opening'),
    path('delete-job-opening/<int:job_id>/', delete_job_opening, name='delete_job_opening'),
]