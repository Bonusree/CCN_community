from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password  # Import this for securely hashing the password
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import User_Details, Blood

# Create your views here.
def home(request):
    return render(request,'home.html')
 

def blood_community(request):
    bloods = Blood.objects.all()
    return render(request, 'blood_community.html',{'bloods':bloods})

def show_alumni(request):
    all_alumni = User_Details.objects.filter(isAlumni=True)
    return render(request,'alumni.html',{'all_alumni':all_alumni})


def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
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
        
        User_Details.objects.create(user=User.objects.get(username=username))
        Blood.objects.create(user=User.objects.get(username=username))
        
        context ={'type':'bg-success','message':'Successfully registered'}
        return render(request,'login.html',context=context)
        
    return render(request,'signup.html')

@login_required
def profile(request):
    if request.method=='POST':
        fullname = request.POST['fullname']
        dept = request.POST['dept']
        session = request.POST['session']
        profession = request.POST['profession']
        profession = True if(profession=='1') else False
        profession_details = request.POST['profession_details']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        last_donate = request.POST['last_donate']
        phone = request.POST['phone']
        
        user = User.objects.get(username=request.user.username)
        if user:
            # update user details 
            _user, created = User_Details.objects.get_or_create(user=user)
            _user.fullName=fullname
            _user.department=dept
            _user.session=session
            if profession_details:
                _user.profession=profession_details
            _user.isAlumni=profession
            _user.address=address
            _user.save()
        
    try:
        user = User.objects.get(username=request.user.username)
        details = User_Details.objects.get(user=user)
        if request.method=="POST":
            # update blood information 
            _blood, created = Blood.objects.get_or_create(user=user,user_details=details)
            if blood_group:
                _blood.blood_group = blood_group
            if last_donate:
                _blood.last_donate = last_donate
            _blood.phone = phone
            _blood.save()
        blood = Blood.objects.get(user=user)
        context={'details':details,'blood':blood}
    except User.DoesNotExist:
        user_details = None
        context={'type':'bg-info','message':'User not found'}
    except User_Details.DoesNotExist:
        context={'type':'bg-info','message':'User details not found'}
        user_details = None
    
    return render(request,'profile.html',context=context)