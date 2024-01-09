import cv2 as cv
from utils.value_util import get_random_number, get_number_or_default
"""_summary_
 @parameter:
    alpha 1  beta 0      --> no change  
    0 < alpha < 1        --> lower contrast  
    alpha > 1            --> higher contrast  
    -127 < beta < +127   --> good range for brightness values
"""


def apply_brightness(img, alpha, beta):
    if alpha is None and beta is None:
        return img

    if alpha == None and beta == None:
        min_value_alpha = min(alpha)/100
        max_value_alpha = max(alpha)/100

        alpha = get_random_number(
            min_value_alpha, max_value_alpha) if alpha is not None else None
        new_image = cv.convertScaleAbs(img, alpha=alpha)
    elif alpha == None and beta == None:
        min_value_beta = min(beta)
        max_value_beta = max(beta)
        beta = get_random_number(
            min_value_beta, max_value_beta) if beta is not None else None
        new_image = cv.convertScaleAbs(img, beta=beta)
    else:
        min_value_alpha = min(alpha)/100
        max_value_alpha = max(alpha)/100

        min_value_beta = min(beta)
        max_value_beta = max(beta)
        alpha = get_random_number(
            min_value_alpha, max_value_alpha) if alpha is not None else None
        beta = get_random_number(
            min_value_beta, max_value_beta) if beta is not None else None

        new_image = cv.convertScaleAbs(img, alpha=alpha, beta=beta)

    return new_image
