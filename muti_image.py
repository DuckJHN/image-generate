import os
from enumeration import extends
import cv2 as cv
folder_dir = "images/"
total_input = 0
images_name = []
list_extend = extends.list_extends
for images in os.listdir(folder_dir):

    if not images.endswith((".png", ".jpg", ".jpeg")):
        continue
    total_input += 1

    images_name.append(images)

    image_path = os.path.join(folder_dir, images)
    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
        continue
    readed_image = cv.imread(image_path)
    cv.imshow("image", readed_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

print(images_name)
print("Total input: ", total_input)
