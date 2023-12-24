from django.urls import path
from . import views

urlpatterns = [
    path('academic/', views.Academic, name='Academic'),
    path('routine/', views.Routine, name='Routine'),
    path('question_bank/', views.Question_bank, name='question_bank'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('academic_notice/', views.academic_notice, name='academic_notice'),
    
]