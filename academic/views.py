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

        Syllabus.objects.filter(syllabus=session).delete()
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
    
from django.shortcuts import render, HttpResponse
from .models import Department, Session, Routine

from django.shortcuts import render, HttpResponse
from .models import Department, Session, Routine

def routine(request):
    try:
        if request.method == 'POST':
            department_name = request.POST['dept_name']
            session_name = request.POST['session']
            pdf_file = request.FILES['pdfFile']
            
            # Check if the department exists
            department, created = Department.objects.get_or_create(department=department_name)

            # Check if the session exists for the department
            session, created = Session.objects.get_or_create(department=department, session_name=session_name)
            print(session)
            # Delete existing Routine data with the same department and session
            try:
                Routine.objects.filter(routine=session).delete()
            except Exception as e:
                print("here delete")
                return HttpResponse(e)
            # Create new Routine entry
            try:
                routine_file = Routine.objects.create(routine=session, pdf_file=pdf_file)
            except Exception as e:
                print("here")
                return HttpResponse(e)
        # Fetch the routine list and department list
        routine_list = Routine.objects.all()
        department_list = Department.objects.all()

        context = {'routine_list': routine_list, 'department_list': department_list}
        return render(request, 'routine.html', context)
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

