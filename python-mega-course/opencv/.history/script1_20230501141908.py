import cv2

img = cv2.imread("galaxy.jpg",0)

print(img.shape[0]/2)
print(img.shape[1]/2)
resized_height = round(img.shape[0]/2,0)
resized_width = round(img.shape[1]/2,0)

resized_img = cv2.resize(img,[resized_height,resized_width])

cv2.imshow("galaxy", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()