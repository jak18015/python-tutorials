import cv2

img = cv2.imread("galaxy.jpg",0)

resized_img = cv2.resize(img,)
cv2.imshow("galaxy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()