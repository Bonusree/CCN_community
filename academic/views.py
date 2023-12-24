from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password  # Import this for securely hashing the password
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Syllabus,Question_bank,Routine, Department, Session

def academic(request):
    if request.method == 'POST':
        department = request.POST['dept_name']
        session=request.POST['session']
        pdf_file = request.FILES['pdfFile']
        
        # Check if the department exists
        department, created = Department.objects.get_or_create(department=department)

        # Check if the session exists for the department
        session, created = Session.objects.get_or_create(department=department, session_name=session)

        # Create a new SyllabusFile instance
        syllabus_file = Syllabus(syllabus=session, pdf_file=pdf_file)
        syllabus_file.save()
    try:
        syllabus_list=Syllabus.objects.all()
        department_list=Department.objects.all()
        for d in department_list:
            print(d.department)
        context={'syllabus_list': syllabus_list, 'department_list':department_list}
        return render(request,'academic.html', context)
    except Exception as e:
        return HttpResponse(e)
    
def routine(request):
    if request.method == 'POST':
        department = request.POST['dept_name']
        session=request.POST['session']
        pdf_file = request.FILES['pdfFile']
        
        # Check if the department exists
        department, created = Department.objects.get_or_create(department=department)

        # Check if the session exists for the department
        session, created = Session.objects.get_or_create(department=department, session_name=session)

        
        routine_file = Routine(routine=session, pdf_file=pdf_file)
        routine_file.save()
    try:
        routine_list=Routine.objects.all()
        department_list=Department.objects.all()
        for d in department_list:
            print(d.department)
        context={'Routine_list': routine_list, 'department_list':department_list}
        return render(request,'routine.html', context)
    except Exception as e:
        return HttpResponse(e)
def question_bank(request):
    if request.method == 'POST':
        department = request.POST['dept_name']
        session=request.POST['session']
        pdf_file = request.FILES['pdfFile']
        
        uploaded_pdf = Question_bank(department=department,session=session, pdf_file=pdf_file)
        uploaded_pdf.save()
        
        return render(request,'question_bank.html')
    return render(request, 'question_bank.html')
def tutorial(request):
    return render(request, 'tutorial.html')
def academic_notice(request):
    return render(request, 'academic_notice.html')

