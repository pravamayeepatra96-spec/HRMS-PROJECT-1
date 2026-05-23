from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.documents_list, name='documents_list'),
    path('documents/add/', views.add_document, name='add_document'),
    path('documents/details/<int:id>/', views.document_details, name='document_details'),
    path('documents/update-status/<int:id>/', views.update_document_status, name='update_document_status'),
    path('documents/delete/<int:id>/', views.delete_document, name='delete_document'),
]