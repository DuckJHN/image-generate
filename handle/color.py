from PIL import Image, ImageEnhance
import numpy as np
import cv2
from itertools import product
import random
import io


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


color_tuple = {
    0: 0,
    'r': 1,
    'g': 2,
    'b': 3
}


def generate_color_combinations_and_random():
    colors = list(color_tuple.values())

    color_combinations = list(product(colors, repeat=3))

    color_combinations = [
        combo for combo in color_combinations if len(set(combo)) > 1
    ]

    if not color_combinations:
        return tuple(color_tuple.values())

    return random.choice(color_combinations)


def apply_change_color(img):
    img = Image.frombytes('RGB', (img.shape[1], img.shape[0]), img.tobytes())

    img = img.convert('RGB')
    combination = generate_color_combinations_and_random()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b = img.getpixel((x, y))
            r, g, b = random_pixel_rgb(combination, r, g, b)
            img.putpixel((x, y), (r, g, b))
    # img.show()
    return img


def random_pixel_rgb(combination, r, g, b):
    _r = 0 if combination[0] == 0 else r if combination[0] == 1 else g if combination[0] == 2 else b
    _g = 0 if combination[1] == 0 else r if combination[1] == 1 else g if combination[1] == 2 else b
    _b = 0 if combination[2] == 0 else r if combination[2] == 1 else g if combination[2] == 2 else b
    return _r, _g, _b


def apply_contrast(image_path, contrast_factor=1.5):
    original_image = Image.open(image_path)

    contrast = ImageEnhance.Contrast(original_image)

    new_image = contrast.enhance(contrast_factor)

    new_image.show()


# apply_change_color('../images/nft3.jpg')
