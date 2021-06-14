import os
import cv2
import face_recognition
# from .models import Encodings
import numpy as np
from pathlib import Path
import csv
# import pandas as pd
            
def encode(path, myfile) :
    RegdNo = myfile.split('.')[0]
    print(RegdNo)
    curImg = cv2.imread(f'{path}')
    Encoding = findEncoding(curImg)
    # print(Encoding)
    print('Encoding Complete') 
    print(Encoding[0])
    with open('C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.csv','r+') as f:
        reader = csv.reader(f)
        for row in reader:
            for r in row :
                r.replace("\n", " ")
        # myDataList = f.readlines()
        # for i in myDataList :
        #     print(i)
        #     i = i.replace('\n', " ")
        #     print(i)
        # print(myDataList)
        print("HIIIII")
        print(myDataList[0])
        print("hii")
        print(myDataList[1])
        f.writelines(f'\n{RegdNo},{Encoding},')
          

def findEncoding(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encoding = face_recognition.face_encodings(image)[0]
    return encoding