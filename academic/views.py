from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password  # Import this for securely hashing the password
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import User_Details, Blood

def Academic(request):
    return render(request,'academic.html')
def Routine(request):
    return render(request, 'routine.html')
def Question_bank(request):
    return render(request, 'question_bank.html')
def tutorial(request):
    return render(request, 'tutorial.html')
def academic_notice(request):
    return render(request, 'academic_notice.html')

