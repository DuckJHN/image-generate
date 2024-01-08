import cv2 as cv


def apply_crop(img):
    mx = (0, 0, 0, 0)
    mx_area = 0
    if img is None:
        return

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

    roi = img[y:y+h, x:x+w]
    return roi
