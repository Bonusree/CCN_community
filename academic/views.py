from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password  # Import this for securely hashing the password
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Syllabus,Question_bank,Routine, Department, Session, Faculty, Tutorial
from django.db import IntegrityError
from CCN_community.decorators import superuser

def tutorial(request):
    
    try:
        if request.method == 'POST':
            department_name = request.POST['department_name']
            faculty=request.POST['faculty']
            course_name=reques.POST['course_name']
            pdf_file = request.FILES['file']
            
            # Check if the department exists
            department, created = Department.objects.get_or_create(department=department_name)

            # Check if the session exists for the department
            faculty, created = Faculty.objects.get_or_create(department=department, faculty_name=faculty)

            Tutorial.objects.filter(tutorial=faculty).delete()
            tutorial_file = Tutorial(tutorial=faculty,course_name=course_name, pdf_file=pdf_file)
            tutorial_file.save()
            tutorial_list=Tutorial.objects.all()
            department_list=Department.objects.all().order_by('department')
            for d in department_list:
                print(d.department)
       
            context={'tutorial_list': tutorial_list, 'department_list':department_list}
            return render(request,'tutorial.html', context)
        tutorial_list=Tutorial.objects.all()
        department_list=Department.objects.all().order_by('department')
        print("i am here")
        context={'tutorial_list': tutorial_list, 'department_list':department_list}
        return render(request,'tutorial.html', context)
    except Exception as e:
            tutorial_list=Tutorial.objects.all()
            department_list=Department.objects.all().order_by('department')
            for d in department_list:
                print(d.department)
       
            context={'tutorial_list': tutorial_list, 'department_list':department_list,'error_message': str(e)}
            return render(request,'tutorial.html', context)


def academic(request):
    try:
        syllabus_list=Syllabus.objects.all().order_by('syllabus')
        department_list=Department.objects.all().order_by('department')
        for d in department_list:
            print(d.department)
       
        context={'syllabus_list': syllabus_list, 'department_list':department_list}
        return render(request,'academic.html', context)
    except Exception as e:
        return HttpResponse(e)


@superuser
def add_syllabus(request):
    try:
        if request.method == 'POST':
            department_name = request.POST['department_name']
            session=request.POST['session']
            pdf_file = request.FILES['pdfFile']
            
            # Check if the department exists
            department, created = Department.objects.get_or_create(department=department_name)

            # Check if the session exists for the department
            session, created = Session.objects.get_or_create(department=department, session_name=session)

            Syllabus.objects.filter(syllabus=session).delete()
            syllabus_file = Syllabus(syllabus=session, pdf_file=pdf_file)
            syllabus_file.save()
            syllabus_list=Syllabus.objects.all().order_by('syllabus')
            department_list=Department.objects.all().order_by('department')
            for d in department_list:
                print(d.department)
       
            context={'syllabus_list': syllabus_list, 'department_list':department_list}
            return render(request,'academic.html', context)
    except Exception as e:
            syllabus_list=Syllabus.objects.all().order_by('syllabus')
            department_list=Department.objects.all().order_by('department')
            for d in department_list:
                print(d.department)
       
            context={'syllabus_list': syllabus_list, 'department_list':department_list,'error_message': str(e)}
            return render(request,'academic.html', context)



       
@superuser
def add_routine(request):
    try:
        if request.method == 'POST':
            department_name = request.POST['department_name']
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
            try:
                # Fetch the routine list and department list
                routine_list = Routine.objects.all().order_by('routine')
                department_list = Department.objects.all().order_by('department')

                context = {'routine_list': routine_list, 'department_list': department_list}
                return render(request, 'routine.html', context)
            except Exception as e:
                return HttpResponse(e)
    except Exception as e:
        routine_list = Routine.objects.all().order_by('routine')
        department_list = Department.objects.all().order_by('department')

        context = {'routine_list': routine_list, 'department_list': department_list,'error_message': str(e)}
        return render(request, 'routine.html', context)




def routine(request):
    try:
        # Fetch the routine list and department list
        routine_list = Routine.objects.all().order_by('routine')
        department_list = Department.objects.all().order_by('department')

        context = {'routine_list': routine_list, 'department_list': department_list}
        return render(request, 'routine.html', context)
    except Exception as e:
        return HttpResponse(e)



def question_bank(request):
    try:
        # Fetch the routine list and department list
        question_list = Question_bank.objects.all().order_by('course_name')
        department_list = Department.objects.all().order_by('department')
        
        context = {'question_list': question_list, 'department_list': department_list}
        return render(request, 'question_bank.html', context)
    except Exception as e:
        return HttpResponse(e)

def add_question(request):
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
            try:
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
                print("here")
                return HttpResponse(e)
    except Exception as e:
       
        # Fetch the routine list and department list
        question_list = Question_bank.objects.all().order_by('course_name')
        department_list = Department.objects.all().order_by('department')
        course_names = [question.course_name for question in question_list]
        for course_name in course_names:
            print(course_name)
       # print(question_list.course_name)
        context = {'question_list': question_list,'course_name':course_name, 'department_list': department_list,'error_message': str(e)}
        return render(request, 'question_bank.html', context)


    

def academic_notice(request):
    return render(request, 'academic_notice.html')

@superuser
def add_new_department(request):
    depts = Department.objects.all()
    if request.method=="POST":
        dept = request.POST.get("dept")
        message = None 
        type = None
        try:    
            if dept:
                Department.objects.create(department=dept)
            else:
                message ='Empty department name'
        except IntegrityError as e:
            message ='Duplicate department name'
        if message:
            type='bg-danger'
        print(message,type)
        return render(request,'add_new_department.html',{"message":message, 'type':type, "depts":depts})
    return render(request,'add_new_department.html',{"depts":depts})

@superuser
def delete_dept(request, dept):
    if dept:
        department = Department.objects.filter(department=dept) 
        department.delete()
    return add_new_department(request)