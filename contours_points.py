import cv2

photo = cv2.imread("images/BMW.jpg")
photo = cv2.resize(photo, (1500, 800))
photo = cv2.Canny(photo, 5, 5)
contours = cv2.findContours(photo, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(contours)
cv2.imshow("test", photo)
cv2.waitKey(0)
