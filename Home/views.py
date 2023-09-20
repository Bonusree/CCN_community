from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def Academic(request):
    return render(request,'academic.html')
def Routine(request):
    return render(request, 'routine.html')
def blood_community(request):
    return render(request, 'blood_community.html')