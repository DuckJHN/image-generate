import cv2 as cv
import math


def apply_crop(img, percentage):
    mx = (0, 0, 0, 0)
    mx_area = 0
    if img is None:
        return
    h_image, w_image, _ = img.shape
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    retval, thresh_gray = cv.threshold(
        gray, thresh=100, maxval=255, type=cv.THRESH_BINARY_INV)

    contours, hierachy = cv.findContours(
        thresh_gray, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for cont in contours:
        x, y, w, h = cv.boundingRect(cont)
        area = w*h

        if area > mx_area:
            mx = x, y, w, h
            mx_area = area

    x, y, w, h = mx

    width_right = math.floor(((w_image - (x+w))*percentage)/100)
    width_left = math.floor(x*(percentage/100))

    roi = img[y:y+h, x-width_left: x+w+width_right]
    return roi
