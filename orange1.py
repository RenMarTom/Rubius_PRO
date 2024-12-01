import cv2
from orange2 import OrangeDetection
from main import KalmanFilter

cap = cv2.VideoCapture("mediafiles/Dima.MOV")
od = OrangeDetection()
kf = KalmanFilter()

while True:
    unk, frame = cap.read()

    box = od.detect(frame)
    print(box)
    x, y, x2, y2 = box
    cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 4)
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)
    cv2.circle(frame, (cx,cy), 25, (0,255,0), 4)
    predicted = kf.prediction(cx,cy)
    cv2.circle(frame,(predicted[0], predicted[1]), 25, (255,0,0), 4)
    cv2.imshow("Dima", frame)
    cv2.waitKey(400)
