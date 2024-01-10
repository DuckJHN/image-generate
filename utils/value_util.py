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


def find_min_max(input_list):
    if not input_list:
        return None, None
    min_value = min(input_list)
    max_value = max(input_list)
    return min_value, max_value


def get_enum_values(enum_class):
    return [member.value for member in enum_class]
