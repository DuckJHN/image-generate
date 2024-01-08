import cv2 as cv
import numpy as np
import random
from enumeration.blur_enum import Blur_Type
from enumeration import blur_enum
from constant.variable import MIN_KERNEL


class NoiseBlur:
    @staticmethod
    def apply_noise(image, max_level):
        if max_level is None:
            return image

        noise_level = np.random.uniform(
            0, max_level, size=(1, 1, image.shape[2]))

        noise = np.random.normal(0, noise_level, size=image.shape)
        noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
        return noisy_image

    @staticmethod
    def apply_blur(image, blur_type='gaussian', max_kernel=5):
        type_exist = blur_enum.check_exist(blur_type.lower())

        if type_exist is None:
            return image
        print("Type: ", type_exist)
        kernel_size = max_kernel if max_kernel > MIN_KERNEL else MIN_KERNEL
        # kernel_size = random.randint(3, max_kernel)

        if Blur_Type.Gaussian == type_exist:
            blurred_image = cv.GaussianBlur(
                image, (kernel_size, kernel_size), 0)
        elif Blur_Type.Median == type_exist:
            blurred_image = cv.medianBlur(image, kernel_size)
        elif Blur_Type.Average == type_exist:
            blurred_image = cv.blur(image, (kernel_size, kernel_size))
        else:
            blurred_image = image

        return blurred_image
