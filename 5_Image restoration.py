import cv2 as cv
import cv2

img = cv2.imread('C:/Users/Rahul/Desktop/Assesment/img/img10.jpg')
mask = cv2.imread('C:/Users/Rahul/Desktop/Assesment/img/img9.jpg', 0)
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

cv2.imwrite('restored.png', dst)