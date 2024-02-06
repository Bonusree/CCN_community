from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password  # Import this for securely hashing the password
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from .models import Syllabus,Question_bank,Routine, Department, Session, Faculty, Tutorial
from django.db import IntegrityError
from CCN_community.decorators import superuser

 
def routine(request):
    try:
        # Fetch the tutorial list and department list
        routine_list = Routine.objects.all().order_by('routine')
        department_list = Department.objects.all().order_by('department')

        context = {'routine_list': routine_list, 'department_list': department_list}
        return render(request, 'routine.html', context)
    except Exception as e:
        return HttpResponse(e)
    
def academic(request):
    try:
        syllabus_list=Syllabus.objects.all().order_by('syllabus')
        department_list=Department.objects.all().order_by('department')
        for d in department_list:
            print(d.department)
       
        context={'syllabus_list': syllabus_list, 'department_list':department_list}
        return render(request,'academic.html', context)
    except Exception as e:
        return HttpResponse(f"exception : {e}")

def question_bank(request):
    try:
        # Fetch the tutorial list and department list
        question_list = Question_bank.objects.all().order_by('course_name')
        department_list = Department.objects.all().order_by('department')
        for q in question_list:
            print(q.course_code, q.course_name, q.session.session_name, q.session.department.department)
        for d in department_list:
            print(d.department)
        context = {'question_list': question_list, 'department_list': department_list}
        print("question")
        return render(request, 'question_bank.html', context)
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

            syllabus_file, create = Syllabus.objects.get_or_create(syllabus=session, pdf_file=pdf_file)
            
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
            semester=request.POST['semester']
            pdf_file = request.FILES['pdfFile']
            semester=str(semester)
            if semester=='1':
                semester+="st "
            elif semester=='2':
                semester+="nd"
            elif semester=='3':
                semester+="rd"
            else:
                semester+="th"
            # Check if the department exists
            department, created = Department.objects.get_or_create(department=department_name)

            # Check if the session exists for the department
            session, created = Session.objects.get_or_create(department=department, session_name=session_name)
            print(session)
            # Delete existing Routine data with the same department and session
            try:
                Routine.objects.filter(routine=session, semester=semester).delete()
            except Exception as e:
                print("here delete")
                return HttpResponse(e)
            # Create new Routine entry
            try:
                routine_file = Routine.objects.create(routine=session,semester=semester, pdf_file=pdf_file)
            except Exception as e:
                print("here")
                return HttpResponse(e)
            return redirect(routine)
    except Exception as e:
        routine_list = Routine.objects.all().order_by('routine')
        department_list = Department.objects.all().order_by('department')

        context = {'routine_list': routine_list, 'department_list': department_list,'error_message': str(e)}
        return render(request, 'routine.html', context)
    
@login_required
def add_question(request):
    try:
        if request.method == 'POST':
            department_name = request.POST['department_name']
            faculty=request.POST['faculty']
            session_name = request.POST['session']
            course_name=request.POST['course_name']
            course_code=request.POST['course_code']
            pdf_file = request.FILES['pdfFile']
            
            # Check if the department exists
            department, created = Department.objects.get_or_create(department=department_name)

            faculty, created = Faculty.objects.get_or_create(department=department, faculty_name=faculty)
            session, created = Session.objects.get_or_create(department=department, session_name=session_name)
            
            try:
                Question_bank.objects.filter(session=session,faculty=faculty,course_code=course_code, course_name=course_name).delete()
            except Exception as e:
                print("here delete")
                return HttpResponse(e)
            # Create new Routine entry
            try:
                question_file =Question_bank.objects.create(session=session,faculty=faculty,course_code=course_code, course_name=course_name, pdf_file=pdf_file)
            except Exception as e:
                print("here")
                return HttpResponse(e)
            try:
                # Fetch the tutorial list and department list
                question_list = Question_bank.objects.all().order_by('course_name')
                department_list = Department.objects.all().order_by('department')
                course_names = [question.course_name for question in question_list]
                for course_name in course_names:
                    print(course_name)
            # print(question_list.course_name)
                context = {'question_list': question_list, 'department_list': department_list}
                return render(request, 'question_bank.html', context)
            except Exception as e:
                print("here")
                return HttpResponse(e)
    except Exception as e:
       
        # Fetch the tutorial list and department list
        question_list = Question_bank.objects.all().order_by('course_name')
        department_list = Department.objects.all().order_by('department')
        
        context = {'question_list': question_list, 'department_list': department_list,'error_message': str(e)}
        return render(request, 'question_bank.html', context)


class TutorialView(View):
    context = {}
    def __init__(self) -> None:
        self.context = {}
        pass
    
    def get(self, request):
        try:
            tutorial_list=Tutorial.objects.all().order_by('course_name')
            depts = Department.objects.all()
            tutorials = {}
            for tut in tutorial_list:
                if tut.dept.department not in tutorials:
                    tutorials[tut.dept.department] = []
                tutorials[tut.dept.department].append(tut)
            self.context['tutorials']= tutorials
            self.context['depts']= depts
            return render(request,'tutorial.html', self.context)
        except Exception as e:
            return HttpResponse(e)
        
    @method_decorator(login_required)
    def post(self,request):
        if request.POST.get('id'):
            id = request.POST.get('id')
            Tutorial.objects.filter(id=id).delete()
            return redirect('tutorial')
        try:
            title = request.POST.get('title')
            dept = request.POST.get('dept')  
            course_name = request.POST.get('course_name')
            course_code = request.POST.get('course_code')
            video_url = request.POST.get('video_url')
                
            # Check if the department exists
            dept = Department.objects.get(department=dept)
            user = User.objects.get(username=request.user)
            tutorial = Tutorial(
                title=title,
                course_name=course_name,
                course_code=course_code,
                video_url=video_url,
                dept = dept,
                added_by = user,
            )
            tutorial.save()
            self.context['message'] = "Successfully added"
            self.context['type']="bg-success"
        except Exception as e:
            self.context['message']=f"error: {e}"
            self.context['type']="bg-danger"
            
        return redirect('tutorial')


@superuser
def delete_syllabus(request):
    try:
        if request.method == 'POST':
            department_name = request.POST['department_name']
            session_name = request.POST['session']
            
            department = Department.objects.filter(department=department_name).last()

            # Check if the session exists for the department
            session= Session.objects.filter(department=department, session_name=session_name).last()
            
            
            try:
                Syllabus.objects.filter(syllabus=session).delete()
            except Exception as e:
                print("here delete")
                return HttpResponse(e)
            
            try:
                # Fetch the tutorial list and department list
                syllabus_list = Syllabus.objects.all().order_by('syllabus')
                department_list = Department.objects.all().order_by('department')

                context = {'syllabus_list': syllabus_list, 'department_list': department_list}
                return render(request, 'academic.html', context)
            except Exception as e:
                return HttpResponse(e)
    except Exception as e:
        syllabus_list = Syllabus.objects.all().order_by('syllabus')
        department_list = Department.objects.all().order_by('department')

        context = {'syllabus_list': syllabus_list, 'department_list': department_list,'error_message': str(e)}
        return render(request, 'academic.html', context)

@superuser
def delete_routine(request):
    try:
        if request.method == 'POST':
            department_name = request.POST['department_name']
            session_name = request.POST['session']
            semester=request.POST['semester']
            department = Department.objects.filter(department=department_name).last()

            session= Session.objects.filter(department=department, session_name=session_name).last()
            print(semester)
            
            try:
                Routine.objects.filter(routine=session,semester=semester).delete()
            except Exception as e:
                print("here delete")
                return HttpResponse(e)
            return redirect(routine)
    except Exception as e:
        routine_list = Routine.objects.all().order_by('routine')
        department_list = Department.objects.all().order_by('department')
        context = {'routine_list': routine_list, 'department_list': department_list,'error_message': str(e)}
        return render(request, 'routine.html', context)

    
@superuser
def delete_question(request):
    try:
        if request.method == 'POST':
            department_name = request.POST['department_name']
            session_name = request.POST['session']
            faculty=request.POST['faculty']
            course_code=request.POST['course_code']
            course_name=request.POST['course_name']
            department = Department.objects.filter(department=department_name).last()

            # Check if the session exists for the department
            session= Session.objects.filter(department=department, session_name=session_name).last()
            faculty= Faculty.objects.filter(department=department, faculty_name=faculty).last()
            
            
            try:
                Question_bank.objects.filter(session=session, faculty=faculty, course_code=course_code, course_name=course_name).delete()
            except Exception as e:
                print("here delete")
                return HttpResponse(e)
            
            return redirect(question_bank)
    except Exception as e:
        question_list = Question_bank.objects.all().order_by('question')
        department_list = Department.objects.all().order_by('department')

        context = {'question_list': question_list, 'department_list': department_list,'error_message': str(e)}
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