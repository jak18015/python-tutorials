import cv2


face_cascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")
img = cv2.imread("Files/photo.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray_img)

