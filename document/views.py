from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeDocument
from user.models import User


def documents_list(request):
    documents = EmployeeDocument.objects.filter(status=1).order_by('-uploaded_date')

    return render(request, 'documents_list.html', {
        'documents': documents
    })


def add_document(request):
    employees = User.objects.filter(status=1).order_by('empid')

    if request.method == "POST":
        employee_id = request.POST.get('employee')
        document_type = request.POST.get('document_type')
        document_file = request.FILES.get('document_file')
        remarks = request.POST.get('remarks')

        employee = get_object_or_404(User, id=employee_id)

        EmployeeDocument.objects.create(
            employee=employee,
            document_type=document_type,
            document_file=document_file,
            remarks=remarks,
            verification_status='Pending'
        )

        return redirect('documents_list')

    return render(request, 'add_document.html', {
        'employees': employees
    })


def document_details(request, id):
    document = get_object_or_404(EmployeeDocument, id=id, status=1)

    return render(request, 'document_details.html', {
        'document': document
    })


def update_document_status(request, id):
    document = get_object_or_404(EmployeeDocument, id=id, status=1)

    if request.method == "POST":
        verification_status = request.POST.get('verification_status')
        remarks = request.POST.get('remarks')

        document.verification_status = verification_status
        document.remarks = remarks
        document.save()

        return redirect('documents_list')

    return render(request, 'update_document_status.html', {
        'document': document
    })


def delete_document(request, id):
    document = get_object_or_404(EmployeeDocument, id=id, status=1)
    document.status = 0
    document.save()

    return redirect('documents_list')