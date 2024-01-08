import cv2 as cv
import numpy as np
import random


def apply_rotation(image, angle=360):
    # angle = np.random.uniform(0, 360)
    height, width = image.shape[:2]
    center = (width / 2, height / 2)
    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv.warpAffine(image, rotation_matrix, (
        width, height), flags=cv.INTER_LINEAR, borderMode=cv.BORDER_REFLECT_101)
    return rotated_image


def apply_flip(image, flip_horizontal, flip_vertical):

    if flip_horizontal and flip_vertical:
        image = cv.flip(image, -1)
    elif flip_horizontal:
        image = cv.flip(image, 1)
    elif flip_vertical:
        image = cv.flip(image, 0)
    return image
