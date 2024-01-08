import cv2 as cv
import numpy as np
from enumeration.blur_enum import Blur_Type
import random


def apply_noise(image, max_level):
    if max_level is None:
        return image

    noise_level = np.random.uniform(0, max_level, size=(1, 1, image.shape[2]))

    noise = np.random.normal(0, noise_level, size=image.shape)
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image


def apply_blur(image, blur_type='guassian', max_kernel=5):
    if blur_type is None:
        return image

    kernel_size = random.randint(3, max_kernel)
    if blur_type is None:
        blurred_image = image

    if Blur_Type.Gaussian.value == blur_type:
        blurred_image = cv.GaussianBlur(image, (kernel_size, kernel_size), 0)
    elif Blur_Type.Median.value == blur_type:
        blurred_image = cv.medianBlur(image, kernel_size)
    elif Blur_Type.Average.value == blur_type:
        blurred_image = cv.blur(image, (kernel_size, kernel_size))

    return blurred_image


# img = cv.imread("nft.png")

# random_type = random.choice(list(Blur_Type))
# random_kernel = random.randint(3, 10)

# img_with_noise = apply_noise(img)

# print("Blur: ", random_type.value)
# print("Kernel: ", random_kernel)

# img_with_blur = apply_blur(
#     img, blur_type=random_type.value, kernel_size=random_kernel)

# cv.imshow("Original", img)

# # cv.imshow("With Noise", img_with_noise)
# cv.imshow("Blurred", img_with_blur)
# cv.waitKey(0)
# cv.destroyAllWindows()
