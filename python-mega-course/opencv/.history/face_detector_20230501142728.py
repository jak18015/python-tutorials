import cv2


face_cascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")
img = cv2.imread("Files/photo.jpg")
gray_img = cv2.cvtColor(img,cv2.color_bgr2gray)

