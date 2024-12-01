import numpy as np
import cv2


class KalmanFilter:
    kf = cv2.KalmanFilter(4, 2)
    kf.transitionMatrix = np.array([[1, 0, 1, 0],
                                    [0, 1, 0, 1],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]], np.float32)
    kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)

    def prediction(self, x, y):
        self.kf.correct(np.array([[x], [y]], np.float32))
        prediction = self.kf.predict()
        return int(prediction[0]), int(prediction[1])
