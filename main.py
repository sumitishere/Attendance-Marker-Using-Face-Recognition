import os
import cv2

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Graphics
imageBackground = cv2.imread('Resources/background.png')

# Importing the mode images into the list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
    # print(imgModeList)

# print(len(imgModeList))
    # print(modePathList)


while True:
    success, img = cap.read()

    # height and width points
    imageBackground[162:162 + 480, 55:55 + 640] = img
    imageBackground[44:44 + 633, 808:808 + 414] = imgModeList[3]
    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Detection", imageBackground)
    cv2.waitKey(1)
