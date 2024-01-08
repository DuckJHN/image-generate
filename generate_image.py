import os
import cv2 as cv
import numpy as np
import handle.rotation_flip as rotation
import handle.crop_image as cr
import handle.resize as rs
import handle.brightness as br
from utils.folder_util import check_folder_or_create
from handle.noise_blur import NoiseBlur as nb
from utils import value_util


def generate(*self, input_path, output_path,
             max_percentage,
             crop,
             max_angle,
             constrast, brightness,
             horizontal=False, vertical=False,
             noise_max_level, blur_type=None, max_kernel,
             limit=1):

    img = cv.imread(input_path, cv.COLOR_BGR2RGB)

    if img is None:
        raise Exception("Img invalid")

    output_path = check_folder_or_create(output_path)
    limit = value_util.get_number_from_str(limit)
    max_angle = value_util.get_number_or_default(value=max_angle, default=0)

    max_percentage = value_util.get_number_or_default(
        value=max_percentage, default=100)

    crop = value_util.get_boolean_or_default(value=crop)

    noise_max_level = value_util.get_number_or_default(
        value=noise_max_level, default=0)

    constrast = (value_util.get_number_or_default(
        value=constrast, default=0))/100
    for x in range(limit):

        # Random
        percentage = value_util.get_random_number(max_percentage, 100)
        if constrast is not None or brightness is not None:
            constrast = value_util.get_random_number(
                constrast - 0.1, constrast + 0.1)
            brightness = value_util.get_random_number(
                brightness - 20, brightness + 20)

        resized_img = rs.apply_resize(img, percentage=percentage)
        if crop:
            resized_img = cr.apply_crop(resized_img.copy())

        rotation_img = rotation.apply_rotation(resized_img, angle=max_angle)
        flipped_img = rotation.apply_flip(
            rotation_img, horizontal, vertical)

        changed_color = br.apply_brightness(
            flipped_img, alpha=constrast, beta=brightness)

        noise_img = nb.apply_noise(
            changed_color, max_level=noise_max_level)
        blurred_image = nb.apply_blur(
            noise_img, blur_type=blur_type, max_kernel=max_kernel)

        output_filename = f"{x + 1}_generated_image.jpg"
        output_filepath = os.path.join(output_path, output_filename)
        cv.imwrite(output_filepath, blurred_image)
