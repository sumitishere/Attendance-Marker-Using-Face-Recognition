import cv2


# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Graphics
imageBackground = cv2.imread('Resources/background.png')


while True:
    success, img = cap.read()

    # height and width points
    imageBackground[162:162+480, 55:55+640] = img

    # cv2.imshow("Webcam", img)

    cv2.imshow("Face Detection", imageBackground)
    cv2.waitKey(1)
