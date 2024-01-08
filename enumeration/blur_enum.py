from enum import Enum


class Blur_Type(Enum):
    Gaussian = 'gaussian',
    Median = 'median',
    Average = 'average',
    Other = 'other'


def list_type():
    list = [bt.value for bt in Blur_Type]
    return [item[0] if isinstance(item, tuple) else item for item in list]


def check_exist(value):
    if value not in list_type():
        return None
    return value
