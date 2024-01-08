import os
import cv2 as cv
import numpy as np
import handle.rotation_flip as rotation
import handle.crop_image as cr
import handle.resize as rs
import handle.brightness as br
from utils.folder_util import check_folder_or_create
import handle.noise_blur as nb
from utils import value_util


def generate(*self, input_path, output_path,
             max_percentage,
             crop,
             max_angle,
             constrast=1, brightness=1, saturation=1, hue=0,
             horizontal=False, vertical=False,
             noise_max_level, blur_type=None, max_kernel,
             limit=1):

    img = cv.imread(input_path, cv.IMREAD_COLOR)

    if img is None:
        raise Exception("Img invalid")

    output_path = check_folder_or_create(output_path)

    limit = value_util.getNumberOrDefault(value=limit, default=1)
    max_angle = value_util.getNumberOrDefault(value=max_angle, default=0)
    max_percentage = value_util.getNumberOrDefault(
        value=max_percentage, default=100)
    crop = value_util.getBooleanOrDefault(value=crop)
    noise_max_level = value_util.getNumberOrDefault(
        value=noise_max_level, default=0)
    max_kernel = value_util.getNumberOrDefault(value=max_kernel, default=5)
    for x in range(limit):

        # Random
        percentage = np.random.uniform(max_percentage, 100)
        angle = np.random.uniform(0, max_angle)

        constrast = np.random.uniform(constrast - 0.1, constrast + 0.1)
        brightness = np.random.uniform(brightness - 20, brightness + 20)

        resized_img = rs.apply_resize(img, percentage=percentage)
        if crop:
            resized_img = cr.apply_crop(resized_img.copy())

        rotation_img = rotation.apply_rotation(resized_img, angle=angle)
        flipped_img = rotation.apply_flip(
            rotation_img, horizontal, vertical)

        changed_color = br.apply_brightness(
            flipped_img, alpha=constrast, beta=brightness)

        noise_img = nb.apply_noise(changed_color, max_level=noise_max_level)
        blur_img = nb.apply_blur(noise_img, blur_type, max_kernel)

        output_filename = f"{x + 1}_generated_image.jpg"
        output_filepath = os.path.join(output_path, output_filename)
        cv.imwrite(output_filepath, blur_img)
