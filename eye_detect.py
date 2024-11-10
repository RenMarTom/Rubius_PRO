import cv2

cap = cv2.VideoCapture("videos/eye_recording.flv")

while True:
    suc, frame = cap.read()
    frame = frame[300:800, 600:1300]

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (7, 7), 0)

    rrr, threshold = cv2.threshold(gray_frame[505:800, 600:1300], 5, 255, cv2.THRESH_BINARY_INV)
    contours, iii = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for con in contours:
        cv2.drawContours(frame, [con], -1, (0, 0, 255), 3)
    print(contours)

    cv2.imshow("Black", threshold)
    cv2.imshow("Gray_eye", gray_frame)
    cv2.imshow("Eye_color", frame)
    cv2.waitKey(150)
