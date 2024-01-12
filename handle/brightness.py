import cv2 as cv
import utils

"""_summary_
 @parameter:
    alpha 1  beta 0      --> no change  
    0 < alpha < 1        --> lower contrast  
    alpha > 1            --> higher contrast  
    -127 < beta < +127   --> good range for brightness values
"""


def apply_brightness(img, alpha=None, beta=None):
    if alpha is None and beta is None:
        return img

    if alpha is not None and beta is None:
        min_value_alpha, max_value_alpha = utils.find_min_max(alpha)

        alpha_processed = utils.get_random_number(
            min_value_alpha/100, max_value_alpha/100) if alpha is not None else None
        new_image = cv.convertScaleAbs(img, alpha=alpha_processed)

    elif alpha is None and beta is not None:
        min_value_beta, max_value_beta = utils.find_min_max(beta)
        beta_processed = utils.get_random_number(
            min_value_beta, max_value_beta) if beta is not None else None
        new_image = cv.convertScaleAbs(img, beta=beta_processed)

    else:
        min_value_alpha, max_value_alpha = utils.find_min_max(alpha)

        min_value_beta, max_value_beta = utils.find_min_max(beta)

        alpha_processed = utils.get_random_number(
            min_value_alpha/100, max_value_alpha/100) if alpha is not None else None
        beta_processed = utils.get_random_number(
            min_value_beta, max_value_beta) if beta is not None else None

        new_image = cv.convertScaleAbs(
            img, alpha=alpha_processed, beta=beta_processed)

    return new_image
