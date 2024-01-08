import numpy as np


def get_number_or_default(value, default):
    value = int(value) if value is not None else default
    return value


def get_boolean_or_default(value):
    value = bool(value) if value is not None else False
    return value


def get_random_number(min_value, max_value):
    return np.random.uniform(min_value, max_value)


def get_number_from_str(string):
    if string is None:
        return 0
    return int(str(string))
