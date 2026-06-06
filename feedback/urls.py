from django.urls import path
from . import views

urlpatterns = [
    path('queries/', views.queries_list, name='queries_list'),
    path('queries/add/', views.add_query, name='add_query'),
    path('queries/reply/<int:id>/', views.reply_query, name='reply_query'),
    path('queries/delete/<int:id>/', views.delete_query, name='delete_query'),

    path('feedback/', views.feedback_list, name='feedback_list'),
    path('feedback/add/', views.add_feedback, name='add_feedback'),
    path('feedback/note/<int:id>/', views.add_feedback_note, name='add_feedback_note'),
    path('feedback/delete/<int:id>/', views.delete_feedback, name='delete_feedback'),
]