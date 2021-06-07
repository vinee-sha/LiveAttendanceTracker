import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
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
from urllib import request
from . import views
# from PIL import ImageGrab

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
    
def markInOuting(regdNo):
    with open('C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/IN.csv','r+') as f:
        myDataList = f.readlines()
        regdList = []
        print("Marked11")
        for line in myDataList:
            entry = line.split(',')
            regdList.append(entry[0])
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime('%H:%M:%S')
        f.writelines(f'\n{regdNo},{date},{time}')

def markOutOuting(regdNo):
    with open('C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/OUT.csv','r+') as f:
        myDataList = f.readlines()
        regdList = []
        print("Marked11")
        for line in myDataList:
            entry = line.split(',')
            regdList.append(entry[0])
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime('%H:%M:%S')
        f.writelines(f'\n{regdNo},{date},{time}')

def OUT() :
    outt = []
    path = 'C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/StudentImages'
    images = []
    studentsRegd = []
    studentsList = os.listdir(path)
    for sl in studentsList:
        curImg = cv2.imread(f'{path}/{sl}')
        images.append(curImg)
        studentsRegd.append(os.path.splitext(sl)[0])
    print(studentsRegd)
    
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    
 
    cap = cv2.VideoCapture(0)
    
    while True:
        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        cv2.imshow('Webcam',img)
        cv2.waitKey(1)
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)
        
            if matches[matchIndex]:
                regdNo = studentsRegd[matchIndex].upper()
                print(regdNo)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,regdNo,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                if regdNo not in outt :
                    markOutOuting(regdNo)
                    outt = outt + [regdNo]
                
        cv2.imshow('Webcam',img)
        k = cv2.waitKey(5000)
        if k == 27:
            cv2.destroyAllWindows()
            break

def IN() :
    #detect = 0
    inn = []
    path = 'C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/StudentImages'
    images = []
    studentsRegd = []
    studentsList = os.listdir(path)
    for sl in studentsList:
        curImg = cv2.imread(f'{path}/{sl}')
        images.append(curImg)
        studentsRegd.append(os.path.splitext(sl)[0])
    print(studentsRegd)
    
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    
 
    cap = cv2.VideoCapture(0)
    
    while True:

        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        cv2.putText(img, 'Click ESC to exit', (10, 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)
        
            if matches[matchIndex]:
                regdNo = studentsRegd[matchIndex].upper()
                print(regdNo)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,regdNo,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                if regdNo not in inn :
                    markInOuting(regdNo)
                    inn = inn + [regdNo]
                #detect = 1
                
        cv2.imshow('Webcam',img)
        k = cv2.waitKey(5000)
        if k == 27:
            cv2.destroyAllWindows()
            break