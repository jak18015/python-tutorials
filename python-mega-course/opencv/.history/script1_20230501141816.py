import cv2

img = cv2.imread("galaxy.jpg",0)

print(img.shape[0]/2)
print(img.shape[1]/2)
resized_height = round(img.shape[0]/2)
# resized_img = cv2.resize(img,[img.shape[0]/2,img.shape[1]/2])
# cv2.imshow("galaxy", resized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()