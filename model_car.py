import cv2
import math
import numpy as np
from object_detection import ObjectDetection

od = ObjectDetection()

cap = cv2.VideoCapture("videos/los_angeles.mp4")
count = 0
center_point_prev_frame = []
tracking_objects = {}
tracking_id = 0

while True:
    ret, frame = cap.read()
    count += 1
    center_point_current_frame = []
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
        (x, y, w, h) = box
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        center_point_current_frame.append((cx, cy))
        print(f'FRAME #{count} {x} {y} {w} {h}')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
        cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)

    for pt in center_point_current_frame:
        for pt2 in center_point_prev_frame:
            distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

            if distance < 20:
                tracking_objects[tracking_id] = pt
                tracking_id += 1

    for object_id, pt in tracking_objects.items():
        cv2.circle(frame, pt, 5, (0, 0, 255), -1)
        cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0, 0, 255), thickness=1)

    print("TR OBJ")
    print(tracking_objects)

    # print('Current frame')
    # print(center_point_current_frame)
    # print('Previous frame')
    # print(center_point_prev_frame)

    center_point_prev_frame = center_point_current_frame
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)
