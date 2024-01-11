import os
import cv2 as cv
import handle.rotation_flip as rotation
import handle.crop_image as cr
import handle.resize as rs
import handle.brightness as br
from handle.noise_blur import NoiseBlur as nb
from utils import value_util
import convert_compress
import numpy as np
from handle.color import apply_change_color, apply_contrast


def generate(*self, input_path, output_path,
             max_percentage,
             crop,
             max_angle,
             constrast, brightness,
             horizontal=False, vertical=False,
             noise_max_level, blur_type=None, max_kernel,
             limit=1):
    if not os.path.exists(input_path):
        raise Exception("Folder not exist")

    for images in os.listdir(input_path):

        if not images.endswith((".png", ".jpg", ".jpeg")):
            continue
        image_path = os.path.join(input_path, images)

        img = cv.imread(image_path)
        if img is None:
            raise Exception("Img invalid")

        limit = value_util.get_number_from_str(limit)

        for x in range(limit):

            changed_crop = cr.apply_crop(img, percentage=crop)
            resized_img = rs.apply_resize(
                changed_crop.copy(), max_percentage=max_percentage)

            rotation_img = rotation.apply_rotation(
                resized_img, angle=max_angle)
            flipped_img = rotation.apply_flip(
                rotation_img, horizontal, vertical)

            changed_brightness = br.apply_brightness(
                flipped_img, alpha=constrast, beta=brightness)

            noise_img = nb.apply_noise(
                changed_brightness, max_level=noise_max_level)
            blurred_image = nb.apply_blur(
                noise_img, blur_type=blur_type, max_kernel=max_kernel)

            changed_color = np.array(apply_change_color(blurred_image))
            changed_contrast = np.array(apply_contrast(changed_color))
            convert_compress.convert_and_compress(
                changed_contrast, output_path)
