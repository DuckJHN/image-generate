from enum import Enum


class ExtendImage(str, Enum):
    JPG = '.jpg'
    PNG = '.png'
    JPEG = '.jpeg'


list_extends = [member.value for member in ExtendImage]
