import cv2 as cv


def nothing(x):
    pass


def apply_resize(img, percentage=100):
    resized = cv.resize(img, (0, 0), fx=percentage/100, fy=percentage/100)
    return resized
