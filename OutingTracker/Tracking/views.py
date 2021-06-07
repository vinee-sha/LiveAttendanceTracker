import os
import zipfile
from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from . import trackouting
import mimetypes
from django.http.response import HttpResponse
import logging
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from zipfile import ZipFile
import shutil

    
def index(request) :
    return render(request,"index.html")

def Login(request) :
    return render(request,"Login.html")

def LoginSubmit(request) :
    if request.method == 'POST':
        AdminID = request.POST['AdminID']
        Password = request.POST['Password']
        if(AdminID == 'admin' and Password == 'admin') :

            return render(request,"UploadCSV.html", {'AdminID':AdminID, 'Password':Password})
        else :
            messages.add_message(request, messages.INFO, 'Invalid Credentials...')
            return render(request,"Login.html")

def UploadCSV(request) :
    return render(request,"UploadCSV.html")

def UploadZIP(request) :
    return render(request,"UploadZIP.html")

def downloadCSV(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'StudentData.csv'
    filepath = BASE_DIR + '/Tracking/media/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def downloadZIP(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'StudentImages.zip'
    filepath = BASE_DIR + '/Tracking/media/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type='application/force-download')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def uploadFile(request):
    if request.method == 'POST' and request.FILES['File_to_upload']:
        os.remove("Tracking/media/StudentData.csv")
        myfile = request.FILES['File_to_upload']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        messages.add_message(request, messages.INFO, 'File Uploaded Successfully...')
        Files = os.listdir("Tracking/media/")
        fileName = "StudentData.csv"
        for file in Files :
            if ".csv" in file :
                fileName = file
        os.rename("Tracking/media/"+fileName, "Tracking/media/StudentData.csv")
        return redirect(UploadCSV)
    else :
        messages.add_message(request, messages.INFO, 'Upload CSV file again...')
    return redirect(UploadCSV)

def uploadFolder(request):
    if request.method == 'POST' and request.FILES['File_to_upload']:
        os.remove("Tracking/media/StudentImages.zip")
        myfile = request.FILES['File_to_upload']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        messages.add_message(request, messages.INFO, 'ZIP Uploaded Successfully...')
        Files = os.listdir("Tracking/media/")
        fileName = "StudentImages.zip"
        for file in Files :
            if ".zip" in file :
                fileName = file
        os.rename("Tracking/media/"+fileName, "Tracking/media/StudentImages.zip")
        shutil.rmtree("Tracking/media/StudentImages")
        zip = ZipFile('Tracking/media/StudentImages.zip')
        zip.extractall('Tracking/media/')
        os.rename("Tracking/media/"+fileName[:-4], "Tracking/media/StudentImages")
        return redirect(UploadZIP)
    else :
        messages.add_message(request, messages.INFO, 'Upload ZIP file again...')    
    return redirect(UploadZIP)

def IN(request) :
    trackouting.IN()
    response = redirect('/Home/')
    return response

def OUT(request) :
    trackouting.OUT()
    response = redirect('/Home/')
    return response
