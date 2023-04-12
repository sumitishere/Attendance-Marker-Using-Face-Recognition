import cv2
import face_recognition
import pickle
import os

# Importing the person images
folderPath = 'Images'
pathList = os.listdir(folderPath)
# print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
    # print(path)
# print(len(imgList))
print(studentIds)


# open cv uses bgr and cvzone uses rgb so convert it
# loop through image and encode every single image
def findEncodings(imgList):
    encodeList = []
    for img in imgList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
# print(encodeListKnown)
print("Encoding Complete!!")

# saving file with picle
file = open("EncodeFile.p",'wb') #open
pickle.dump(encodeListKnownWithIds,file) #dump
file.close() #close
print("File Saved")

