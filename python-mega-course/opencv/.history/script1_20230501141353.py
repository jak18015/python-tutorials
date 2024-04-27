import cv2

img = cv2.imread("galaxy.jpg",1)

print(type(img))
print(img.shape)
print(img.ndim)
print(img)

