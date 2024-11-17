import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    suc, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    height, width, i = frame.shape
    cx = int(width / 2)
    cy = int(height / 2)

    pixel_center = hsv_frame[cx, cy]
    h_value = pixel_center[0]

    color = "undefinied"
    if h_value < 7:
        color = "red"
    elif h_value < 17:
        color = "orange"
    elif h_value < 32:
        color = "yellow"
    elif h_value < 73:
        color = "green"
    elif h_value < 131:
        color = "blue"
    elif h_value < 142:
        color = "purple"
    elif h_value < 164:
        color = "pink"
    else:
        color = "red"

    cv2.circle(frame, (cx, cy), 5, (255, 0, 0))
    cv2.putText(frame, color, (cx - 200, cy - 200),
                0, 3, (255, 0, 0), 3)
    cv2.imshow("cap", frame)
    cv2.waitKey(1)
