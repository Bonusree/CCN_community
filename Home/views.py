from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password  # Import this for securely hashing the password
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

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
def blood_community(request):
    return render(request, 'blood_community.html')

def show_alumni(request):
    return render(request,'alumni.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        print("----------------",username,password)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If user is authenticated, log them in
            login(request, user)
            return redirect('home') 
        else:
            context ={'type':'bg-danger','message':'Invalid username or password'}
            return render(request, 'login.html', context=context)
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirmPassword']
        
        # check password 
        if password!=cpassword:
            context ={'type':'bg-danger','message':'Password missmatched!'}
            print("missmatched")
            return render(request,'signup.html',context=context)
        
        # check user email 
        if User.objects.filter(email=email).exists():
            context ={'type':'bg-warning','message':'Already registered'}
            return render(request,'signup.html',context=context)
        
        # Hash the password securely
        # hashed_password = make_password(password)
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        
        context ={'type':'bg-success','message':'Successfully registered'}
        return render(request,'login.html',context=context)
        
    return render(request,'signup.html')

def profile(request):
    return render(request,'profile.html')
    pass