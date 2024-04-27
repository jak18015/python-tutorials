import cv2

img = cv2.imread("galaxy.jpg",0)

print(img.shape[0]/2)
print(img.shape[1]/2)

resized_img = cv2.resize(img,[int(img.shape[1]/2),int(img.shape[0]/2)])

cv2.imwrite("galaxy_2", resized_img)

cv2.imshow("galaxy_2", resized_img)
cv2.imshow("galaxy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()