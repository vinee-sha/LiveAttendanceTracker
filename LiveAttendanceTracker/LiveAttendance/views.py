#import LiveAttendance.attendance
from django.shortcuts import render
import os

# Create your views here.
def index(request) :
    return render(request,"index.html")

def StudentLogin(request) :
    return render(request,"StudentLogin.html")

def TeacherLogin(request) :
    return render(request,"TeacherLogin.html")

def StudentRegister(request) :
    return render(request,"StudentRegister.html")

def TeacherRegister(request) :
    return render(request,"TeacherRegister.html")