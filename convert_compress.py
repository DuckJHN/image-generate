import cv2 as cv
import random
import os
import uuid
import time
import calendar
import exif
from datetime import datetime


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# providing some information
user_comment = "random image"
software = "created in python with numpy"
author = "Rune Monzel"


def check_folder_or_create(path):
    is_exist = os.path.exists(path)
    if not is_exist:
        os.makedirs(path)
    return path


current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)


def convert_and_compress(image, output_path):
    output_path = check_folder_or_create(output_path)

    format = random.choice(['JPG', 'PNG'])
    compression_level = 100
    if format in ['JPEG', 'JPG']:
        compression_params = [int(
            cv.IMWRITE_JPEG_QUALITY), compression_level] if compression_level is not None else None
    elif format == 'PNG':
        compression_level = 9
        compression_params = [int(cv.IMWRITE_PNG_COMPRESSION),
                              compression_level] if compression_level is not None else None

    output_filename = f"{time_stamp}-{uuid.uuid1()}.{format.lower()}"
    output_filepath = os.path.join(output_path, output_filename)

    status, abc = cv.imencode('.jpg', image)
    exif_jpg = exif.Image(abc.tobytes())

    exif_jpg.datetime_original = random_date(
        "1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())
    exif_jpg.datetime_digitized = random_date(
        "1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())

    with open(output_filepath, 'wb') as new_image_file:
        new_image_file.write(exif_jpg.get_file())
        print(
            f"Image saved successfully to '{output_path}' in {format} format. => {output_filename}")


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)
