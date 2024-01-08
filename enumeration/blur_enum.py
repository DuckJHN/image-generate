from enum import Enum


class Blur_Type(str, Enum):
    GAUSSIAN = 'gaussian'
    MEDIAN = 'median'
    AVERAGE = 'average'
    OTHER = 'other'

    def equals(self, string):
        return self.name == string


def list_type():
    return [bt.value for bt in Blur_Type]


def check_exist(value):
    if value not in list_type():
        return None
    return next(member for member in Blur_Type if member.value == value).name
