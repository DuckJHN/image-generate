import cv2 as cv
from utils import value_util


def nothing(x):
    pass


def apply_resize(img, max_percentage):
    if max_percentage == 100:
        return img
    min_value = min(max_percentage)
    max_value = max(max_percentage)
    percentage = value_util.get_random_number(min_value, max_value)
    resized = cv.resize(img, (0, 0), fx=percentage/100, fy=percentage/100)
    return resized
