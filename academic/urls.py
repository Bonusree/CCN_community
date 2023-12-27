from django.urls import path
from . import views

tutorial = views.TutorialView()

urlpatterns = [
    path('syllabus/', views.academic, name='academic'),
    path('syllabus/add_syllabus/', views.add_syllabus, name='add_syllabus'),
    path('syllabus/delete_syllabus', views.delete_syllabus, name='delete_syllabus'),
  
    path('routine/delete_routine', views.delete_routine, name='delete_routine'),
    path('add_routine/', views.add_routine, name='add_routine'),
    path('routine/', views.routine, name='routine'),
  
    path('question_bank/delete_question_bank', views.delete_question, name='delete_question'),
    path('add_question/', views.add_question, name='add_question'),
    path('routine/', views.routine, name='routine'),
    path('question_bank/', views.question_bank, name='question_bank'),
    
    path('tutorial/', views.TutorialView.as_view() , name='tutorial'),
    path('tutorial/add-new/', views.TutorialView.as_view(), name='add_tutorial'),
    
    path('academic_notice/', views.academic_notice, name='academic_notice'),
    path('add-new-department/', views.add_new_department, name='new_dept'),
    path('delete-department/<str:dept>/', views.delete_dept, name='delete_dept'),
    
]