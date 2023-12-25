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
        syllabus_list=Syllabus.objects.all().order_by('syllabus')
        department_list=Department.objects.all().order_by('department')
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
        routine_list = Routine.objects.all().order_by('routine')
        department_list = Department.objects.all().order_by('department')

        context = {'routine_list': routine_list, 'department_list': department_list}
        return render(request, 'routine.html', context)
    except Exception as e:
        return HttpResponse(e)


def question_bank(request):
    try:
        if request.method == 'POST':
            department_name = request.POST['department_name']
            session_name = request.POST['session']
            course_name=request.POST['course_name']
            pdf_file = request.FILES['pdfFile']
            
            # Check if the department exists
            department, created = Department.objects.get_or_create(department=department_name)

            # Check if the session exists for the department
            session, created = Session.objects.get_or_create(department=department, session_name=session_name)
            print(session)
            # Delete existing Routine data with the same department and session
            try:
                Question_bank.objects.filter(question=session, course_name=course_name).delete()
            except Exception as e:
                print("here delete")
                return HttpResponse(e)
            # Create new Routine entry
            try:
                question_file =Question_bank.objects.create(question=session, course_name=course_name, pdf_file=pdf_file)
            except Exception as e:
                print("here")
                return HttpResponse(e)
        # Fetch the routine list and department list
        question_list = Question_bank.objects.all().order_by('course_name')
        department_list = Department.objects.all().order_by('department')
        course_names = [question.course_name for question in question_list]
        for course_name in course_names:
            print(course_name)
       # print(question_list.course_name)
        context = {'question_list': question_list,'course_name':course_name, 'department_list': department_list}
        return render(request, 'question_bank.html', context)
    except Exception as e:
        return HttpResponse(e)

def tutorial(request):
    return render(request, 'tutorial.html')
def academic_notice(request):
    return render(request, 'academic_notice.html')

