import cv2 as cv

"""_summary_
 @parameter:
    Alpha is contrast
        low: 0 -1
        hight: > 1
    Beta is brightness in value [-127, 127]
"""

# for y in range(img.shape[0]):
#     for x in range(img.shape[1]):
#         for c in range(img.shape[2]):
#             new_image[y, x, c] = np.clip(alpha * img[y, x, c] + beta, 0, 255)


def apply_brightness(img, alpha, beta):
    if alpha == None & beta == None:
        return img

    new_image = cv.convertScaleAbs(img, alpha=alpha, beta=beta)
    return new_image
