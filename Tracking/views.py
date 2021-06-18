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
import csv
from . import encodeImage

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

def UploadImages(request) :
    return render(request,"UploadImages.html")

def downloadCSV(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'StudentData.csv'
    filepath = BASE_DIR + '/Tracking/media/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
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

def uploadFiles(request):
    if request.method == 'POST' and request.FILES.getlist('Files_to_upload'):
        myfiles = request.FILES.getlist('Files_to_upload')
        fs = FileSystemStorage()
        for myfile in myfiles : 
            filename = fs.save("StudentImages/"+myfile.name, myfile)
            encodeImage.encode("Tracking/media/StudentImages/"+ myfile.name, myfile.name)
        messages.add_message(request, messages.INFO, 'File Uploaded Successfully...')
        return redirect(UploadImages)
    else :
        messages.add_message(request, messages.INFO, 'Upload images again...')
    return redirect(UploadImages)

def deleteFiles(request) :
    Files_to_delete = request.POST['Files_to_delete']
    if request.method == 'POST' and Files_to_delete:
        deleted = 0
        Files_to_delete = Files_to_delete.split(',')
        for files in Files_to_delete :
            files = files.strip()
        Files = os.listdir("Tracking/media/StudentImages")
        for file in Files :
            fileName = file.split('.')[0]
            if fileName in Files_to_delete :
                deleted += 1
                os.remove("Tracking/media/StudentImages/"+file)
                RegdNo = []
                Name = []
                ParentPhn = []
                with open('Tracking/media/StudentData.csv', 'r') as readFile:
                    reader = csv.reader(readFile)
                    for row in reader:
                        if row[0] != fileName:
                            RegdNo.append(row[0])
                            Name.append(row[1])
                            ParentPhn.append(row[2])
                with open('Tracking/media/StudentData.csv', 'w', newline="") as f:
                    length = len(RegdNo)-1
                    for i in range(length) :
                        f.writelines(f'{RegdNo[i]},{Name[i]},{ParentPhn[i]}\n')
                    f.writelines(f'{RegdNo[length]},{Name[length]},{ParentPhn[length]}')
        if(deleted != 0) :
            messages.add_message(request, messages.INFO, 'Files Deleted Successfully...')
        else :
            messages.add_message(request, messages.INFO, 'Files were not deleted...')
        return redirect(deleteImages)
    else :
        messages.add_message(request, messages.INFO, 'Sorry, Try again...')
    return redirect(deleteImages)

def deleteImages(request) :
    return render(request,"DeleteImages.html")

def IN(request) :
    trackouting.IN()
    response = redirect('/Home/')
    return response

def OUT(request) :
    trackouting.OUT()
    response = redirect('/Home/')
    return response

def regdNoSubmit(request) :
    if request.method == 'POST':
        regdNo = request.POST['regdNo']
        InDate = []
        InTime = []
        with open("Tracking/media/IN.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if(row[0]==regdNo):
                    InDate += [row[1]]
                    InTime += [row[2]]
        OutDate = []
        OutTime = []
        with open("Tracking/media/OUT.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if(row[0]==regdNo):
                    OutDate += [row[1]]
                    OutTime += [row[2]]
        return render(request,"regdNoSearch.html",{"regdNo":regdNo, "InDate":InDate, "InTime":InTime, "OutDate":OutDate, "OutTime":OutTime})
    else:
        messages.add_message(request, messages.INFO, 'Sorry, Try again...')
        return render(request,"UploadCSV.html")

def dateSubmit(request) :
    if request.method == 'POST':
        Date = request.POST['Date']
        InRegdNo = []
        InTime = []
        with open("Tracking/media/IN.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if(row[1]== Date):
                    InRegdNo += [row[0]]
                    InTime += [row[2]]
        OutRegdNo = []
        OutTime = []
        with open("Tracking/media/OUT.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if(row[1]==Date):
                    OutRegdNo += [row[0]]
                    OutTime += [row[2]]
        return render(request,"dateSearch.html",{"OutRegdNo":OutRegdNo, "Date":Date, "InTime":InTime, "InRegdNo":InRegdNo, "OutTime":OutTime})
    else:
        messages.add_message(request, messages.INFO, 'Sorry, Try again...')
        return render(request,"UploadCSV.html")