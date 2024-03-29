import os
import time
import cv2 as cv
import numpy as np
import handle.rotation_flip as rotation
import handle.crop_image as cr
import handle.resize as rs
import handle.brightness as br
from handle.noise_blur import NoiseBlur as nb
from utils import value_util
import convert_compress
from handle.color import apply_change_color, apply_contrast
import concurrent.futures

start_time = time.time()


def process_image(image_path, output_path, max_percentage, crop, max_angle, constrast, brightness, color,
                  horizontal, vertical, noise_max_level, blur_type, max_kernel, limit):
    img = cv.imread(image_path)
    if img is None:
        raise cv.error(f"Can not read image: {image_path}.")

    limit = value_util.get_number_from_str(limit)
    for x in range(limit):
        changed_crop = cr.apply_crop(img, percentage=crop)
        resized_img = rs.apply_resize(
            changed_crop, max_percentage=max_percentage)

        rotation_img = rotation.apply_rotation(resized_img, angle=max_angle)
        flipped_img = rotation.apply_flip(rotation_img, horizontal, vertical)

        changed_brightness = br.apply_brightness(
            flipped_img, alpha=constrast, beta=brightness)

        noise_img = nb.apply_noise(
            changed_brightness, max_level=noise_max_level)
        blurred_image = nb.apply_blur(
            noise_img, blur_type=blur_type, max_kernel=max_kernel)

        if color:
            blurred_image = np.array(apply_change_color(blurred_image))
        changed_contrast = np.array(apply_contrast(blurred_image))
        convert_compress.convert_and_compress(changed_contrast, output_path)


def generate_from_folder(input_path, output_path, max_percentage, crop, max_angle, constrast, brightness, color,
                         horizontal=False, vertical=False, noise_max_level=0, blur_type=None, max_kernel=1, limit=1, batch_size=10):

    image_paths = [os.path.join(input_path, image) for image in os.listdir(input_path)
                   if image.lower().endswith((".png", ".jpg", ".jpeg"))]
    limit = value_util.get_number_from_str(limit)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(0, len(image_paths), batch_size):
            batch_paths = image_paths[i:i + batch_size]

            futures = []
            for image_path in batch_paths:
                futures.append(executor.submit(process_image, image_path, output_path, max_percentage, crop,
                                               max_angle, constrast, brightness, color, horizontal, vertical,
                                               noise_max_level, blur_type, max_kernel, limit))

            concurrent.futures.wait(futures)
    calculate_time()


def calculate_time():
    print("-----%s seconds ----" % (time.time() - start_time))
