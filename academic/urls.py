from django.urls import path
from . import views

urlpatterns = [
    path('academic/', views.academic, name='academic'),
    path('routine/', views.routine, name='routine'),
    path('question_bank/', views.question_bank, name='question_bank'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('academic_notice/', views.academic_notice, name='academic_notice'),
    
]