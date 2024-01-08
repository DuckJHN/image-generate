import os
import cv2 as cv

folder_dir = "./"
total_input = 0
images_name = []
for images in os.listdir(folder_dir):

    if (images.endswith(".png") or images.endswith(".jpg")
            or images.endswith(".jpeg")):
        total_input += 1
        print(images)
        images_name.append(images)
        readed_image = cv.imread(images)
        cv.imshow("image", readed_image)
        cv.waitKey(0)
        cv.destroyAllWindows()
print("Total input: ", total_input)
