import cv2 as cv
import handle.rotation_flip as rotation
import handle.crop_image as cr
import handle.resize as rs
import handle.brightness as br
from handle.noise_blur import NoiseBlur as nb
from utils import value_util
import convert_compress


def generate(*self, input_path, output_path,
             max_percentage,
             crop,
             max_angle,
             constrast, brightness,
             horizontal=False, vertical=False,
             noise_max_level, blur_type=None, max_kernel,
             limit=1):

    img = cv.imread(input_path)

    if img is None:
        raise Exception("Img invalid")

    limit = value_util.get_number_from_str(limit)

    crop = value_util.get_boolean_or_default(value=crop)

    for x in range(limit):

        resized_img = rs.apply_resize(img, max_percentage=max_percentage)
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

        convert_compress.convert_and_compress(blurred_image, output_path)
