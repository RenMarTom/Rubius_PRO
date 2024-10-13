import cv2
import numpy as np

img = cv2.imread("images/bmw.jpg")
new_img = cv2.resize(img, (1500, 800))
new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
new_img = cv2.Canny(new_img, 100, 100)
kernel = np.ones((2, 2), np.uint8)
new_img = cv2.dilate(new_img, kernel, 1)
cv2.imshow("BMW", new_img)
cv2.waitKey(0)
