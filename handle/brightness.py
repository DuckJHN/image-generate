import cv2 as cv

"""_summary_
 @parameter:
    alpha 1  beta 0      --> no change  
    0 < alpha < 1        --> lower contrast  
    alpha > 1            --> higher contrast  
    -127 < beta < +127   --> good range for brightness values
"""

# for y in range(img.shape[0]):
#     for x in range(img.shape[1]):
#         for c in range(img.shape[2]):
#             new_image[y, x, c] = np.clip(alpha * img[y, x, c] + beta, 0, 255)


def apply_brightness(img, alpha, beta):
    if alpha == None and beta == None:
        return img

    new_image = cv.convertScaleAbs(img, alpha=alpha, beta=beta)
    return new_image
