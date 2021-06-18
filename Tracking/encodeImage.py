import os
import cv2
import face_recognition
import numpy as np
from pathlib import Path
import csv
            
def encode(path, myfile) :
    RegdNo = myfile.split('.')[0]
    curImg = cv2.imread(f'{path}')
    Encoding = findEncoding(curImg)
    with open('C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.csv','a') as f:
        f.writelines(f'\n{RegdNo},{Encoding}')

def findEncoding(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encoding = face_recognition.face_encodings(image)[0]
    return encoding