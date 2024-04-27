import cv2


face_cascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")
img = cv2.imread("Files/photo.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.05,
                                      minNeighbors=5)

print(faces)

cv2.imshow("gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

