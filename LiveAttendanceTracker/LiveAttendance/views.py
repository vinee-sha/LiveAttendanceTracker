import os
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import *
from . import SendEmail

# Create your views here.
def index(request) :
    return render(request,"index.html")

def StudentLogin(request) :
    return render(request,"StudentLogin.html")

def StudentLoginSubmit(request) :
    if request.method == 'POST':
        RegdNo = request.POST['RegdNo']
        Password = request.POST['Password']
        try :
            data = Student.objects.get(RegdNo=RegdNo, Password=Password)
            if data: 
                return render(request,"StudentEditDetails.html", {'data':data})
            else :
                messages.add_message(request, messages.INFO, 'Invalid Credentials..')
        except Exception as e :
            messages.add_message(request, messages.INFO, 'Invalid Credentials..')
    return render(request,"StudentLogin.html")

def StudentRegister(request) :
    return render(request,"StudentRegister.html")

def StudentRegisterSubmit(request) :
    if request.method == 'POST':
        RegdNo = request.POST['RegdNo']
        Email = request.POST['Email']
        Branch = request.POST['Branch']
        Batch = request.POST['Batch']
        Section = request.POST['Section']
        Password = request.POST['Password']
        try :
            Student(RegdNo=RegdNo, Email=Email, Branch=Branch, Batch=Batch, Section=Section, Password=Password).save()
            data = Student.objects.get(RegdNo=RegdNo)
            if data:
                return render(request,"StudentEditDetails.html", {'data':data})
            else :
                messages.add_message(request, messages.INFO, 'Invalid Registration')
        except Exception as e :
            messages.add_message(request, messages.INFO, 'Invalid Registration')
    return render(request,"StudentRegister.html")


def TeacherLogin(request) :
    return render(request,"TeacherLogin.html")

def TeacherLoginSubmit(request) :
    if request.method == 'POST':
        TeacherId = request.POST['TeacherId']
        Password = request.POST['Password']
        try :
            data = Teacher.objects.get(TeacherId=TeacherId, Password=Password)
            if data: 
                return render(request,"TeacherEditDetails.html", {'data':data})
            else :
                messages.add_message(request, messages.INFO, 'Invalid Credentials..')
        except Exception as e :
            messages.add_message(request, messages.INFO, 'Invalid Credentials..')
    return render(request,"TeacherLogin.html")

def TeacherRegister(request) :
    return render(request,"TeacherRegister.html")

def TeacherRegisterSubmit(request) :
    if request.method == 'POST':
        TeacherId = request.POST['TeacherId']
        Email = request.POST['Email']
        Branch = request.POST['Branch']
        Password = request.POST['Password']
        try :
            Teacher(TeacherId=TeacherId, Email=Email, Branch=Branch, Password=Password).save()
            data = Teacher.objects.get(TeacherId=TeacherId)
            if data:
                return render(request,"TeacherEditDetails.html", {'data':data})
            else :
                messages.add_message(request, messages.INFO, 'Invalid Registration')
        except Exception as e :
            messages.add_message(request, messages.INFO, 'Invalid Registration')
    return render(request,"TeacherRegister.html")


def ForgotPassword(request) :
    return render(request,"ForgotPassword.html")

def ForgotPasswordSubmit(request) :
    if request.method == 'POST':
        Email = request.POST['Email']
        try :
            data1 = Teacher.objects.get(Email=Email)
            if(data1) :
                Username = data1.TeacherId
                Password = data1.Password
                SendEmail.send_mail(Email, Username, Password)
        except Exception as e :
            try:
                data2 = Student.objects.get(Email=Email)
                if(data2) :
                    Username = data2.RegdNo
                    Password = data2.Password
                    SendEmail.send_mail(Email, Username, Password)
            except Exception as e :
                print(e)
    return render(request,"details.html")


def TeacherEdit(request) :
    return render(request,"TeacherEditDetails.html")

def TeacherEditSubmit(request) :
    if request.method == 'POST':
        TeacherId = request.POST['TeacherId']
        Email = request.POST['Email']
        Password = request.POST['Password']
        try :
            data = Teacher.objects.get(TeacherId=TeacherId)
            if data:
                data.Email=Email
                data.Password=Password
                data.save()
            return render(request,"details.html", {'data':data})
        except Exception as e :
            messages.add_message(request, messages.INFO, 'Details not Updated!')
    return render(request,"TeacherEditDetails.html")

def StudentEdit(request) :
    return render(request,"StudentEditDetails.html")

def StudentEditSubmit(request) :
    if request.method == 'POST':
        RegdNo = request.POST['RegdNo']
        Email = request.POST['Email']
        Password = request.POST['Password']
        try :
            data = Student.objects.get(RegdNo=RegdNo)
            if data:
                data.Email=Email
                data.Password=Password
                data.save()
            return render(request,"details.html", {'data':data})
        except Exception as e :
            messages.add_message(request, messages.INFO, 'Details not Updated!')
    return render(request,"StudentEditDetails.html")