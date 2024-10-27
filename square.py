import cv2
import numpy as np

photo = np.zeros((600, 600, 3), dtype="uint8")
cv2.line(photo, (5,5), (5,100), (0,255,0), thickness=1)
cv2.line(photo, (100,5), (100,100), (0,255,0), thickness=1)
cv2.line(photo, (5,5), (100,5), (0,255,0), thickness=1)
cv2.line(photo, (100,100), (100,100), (0,255,0), thickness=1)
cv2.line(photo, (5,5), (100,100), (0,255,0), thickness=1)
cv2.line(photo, (5,100), (100,5), (0,255,0), thickness=1)
cv2.line(photo, (5,100), (100,100), (0,255,0), thickness=1)
cv2.imshow("test", photo)
cv2.waitKey(0)
