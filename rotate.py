import cv2


def rotate(img, angle):
    height, width = img.shape[0:2]
    point = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img, matrix, (width, height))


photo = cv2.imread("images/BMW.jpg")
photo = cv2.resize(photo, (1500, 800))
i = 0
while True:
    i += 1
    photo1 = rotate(photo, i)
    cv2.imshow("test", photo1)
    cv2.waitKey(1)
