import cv2
import numpy as np


def adjust_color(image, brightness=None, contrast=None, saturation=None, hue=None):
    img_float = image.astype(np.float32) / 255.0

    if brightness is not None:
        img_float += brightness

    if contrast is not None:
        img_float *= contrast

    hsv = cv2.cvtColor(img_float, cv2.COLOR_BGR2HSV)
    if saturation is not None:
        hsv[:, :, 1] *= saturation
    if hue is not None:
        hsv[:, :, 0] += hue
        hsv[:, :, 0] = np.clip(hsv[:, :, 0], 0, 179)

    img_result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    img_result = np.clip(img_result * 255, 0, 255).astype(np.uint8)

    return img_result


img = cv2.imread("nft2.jpg")

random_brightness = np.random.uniform(-0.5, 0.5)
random_contrast = np.random.uniform(0.1, 1.5)
random_saturation = np.random.uniform(0.1, 1.5)
random_hue = np.random.uniform(-20, 20)

# brightness = float(input('Brightness: '))
# constrast = float(input('Constrast: '))
# saturation = float(input('Saturation: '))
# hue = float(input('Hue: '))


img_adjusted = adjust_color(img, brightness=random_brightness,
                            contrast=random_contrast, saturation=random_saturation, hue=random_hue)

cv2.imshow("Original", img)
cv2.imshow("Adjusted", img_adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()
