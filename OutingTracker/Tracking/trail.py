# import numpy 
# import pickle

# arr=numpy.array([numpy.array([1,2,3,4]),numpy.array([9,7,7,8])])
# #saving arr as a .pickle file externally, wb-write binary
# pickle.dump(arr,open("C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.pickle","wb"))

# #Below is to read and retrieve its contents, rb-read binary
# with open("C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.pickle", "rb") as f:
#     X = pickle.load(f, encoding="latin1") 
#     print(X.files)


# import os
# import cv2
# import face_recognition
# # from .models import Encodings
# import numpy as np
# from pathlib import Path
# # import pandas as pd
            
# def encode(path, myfile) :
#     RegdNo = myfile.split('.')[0]
#     print(RegdNo)
#     curImg = cv2.imread(f'{path}')
#     Encoding = findEncoding(curImg)
#     # print(Encoding)
#     print('Encoding Complete') 
#     print(Encoding[0])
#     p = Path('C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.npy')
#     with p.open('ab') as f:
#         np.savez(f, Encoding)
#     # np.save('C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.npy', Encoding) # save
#     new_num_arr = np.load(p,allow_pickle=True,fix_imports=True,encoding='latin1') # load
#     print(new_num_arr.files)
#     print("Hii")

#     # a = np.array([1,2,3,4])
#     # with p.open('wb') as f:
#     #     np.savez(f, a=a)
#     # new_num_arr = np.load(p,allow_pickle=True,fix_imports=True,encoding='latin1') # load
#     # print(new_num_arr[a])
#     # with open('C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.csv','r+') as f:
#     #     myDataList = f.readlines()
#     #     f.writelines(f'\n{RegdNo},{Encoding}')
#     # Encoding.dump("C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.dat")
#     # mat2 = np.load("C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.dat")
#     # print(mat2)
#     # Encoding.dump("C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.pkl")
#     # mat = np.load("C:/Users/user/Desktop/New folder/OutingTracker/Tracking/media/EncodingData.pkl")
#     # print(mat)
    
#     #Encoding = Encoding.tostring()
#     # try :
#     #     Encodings(RegdNo = RegdNo, Encoding = Encoding).save()
#     #     print("Encoding done for " + RegdNo)
#     # except Exception as e :
#     #     print(e)
#     #     print("Encoding not done for " + RegdNo)

# def findEncoding(image):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     encoding = face_recognition.face_encodings(image)[0]
#     return encoding